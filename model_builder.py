import pandas as pd
import numpy as np
import os
import pickle

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score

# 1. Cargar dataset
df = pd.read_csv("data/smartphone_segments.csv")

# 2. Limpiar y preparar datos
df.dropna(inplace=True)
X = df.drop("segment", axis=1)
y = df["segment"]

# 3. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Crear pipeline con preprocesamiento y modelos
models = {
    "RandomForest": RandomForestClassifier(random_state=42),
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "SVM": SVC()
}

best_score = 0
best_model = None
best_name = ""

for name, model in models.items():
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', model)
    ])
    
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="weighted")
    print(f"{name} → Accuracy: {acc:.3f}, F1-score: {f1:.3f}")

    if f1 > best_score:
        best_score = f1
        best_model = pipeline
        best_name = name

# 5. Guardar mejor modelo
if not os.path.exists("models"):
    os.makedirs("models")

with open("models/best_model.pkl", "wb") as f:
    pickle.dump(best_model, f)

print(f"\nModelo guardado: {best_name} con F1 = {best_score:.3f}")
