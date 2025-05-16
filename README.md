# Clasificador de Segmentos de Smartphones

Este proyecto es una aplicación web desarrollada con FastAPI, que permite al usuario ingresar las características técnicas de un smartphone y obtener el segmento de mercado al que pertenece: Budget, Midrange o Premium.

La aplicación utiliza un modelo de Machine Learning previamente entrenado y proporciona tanto una interfaz gráfica como un endpoint API para predicciones externas.

## Funcionalidades

- Predicción del segmento del smartphone a partir de sus especificaciones técnicas
- Entrenamiento y evaluación del modelo (Random Forest, Logistic Regression, SVM)
- Interfaz web moderna con formulario interactivo
- Endpoint de predicción JSON accesible desde Thunder Client, Postman o scripts externos

## Tecnologías utilizadas

- Python 3.10+
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- Jinja2 (HTML templates)
- Uvicorn
- HTML + CSS

## Estructura del proyecto

```
SmartPhoneSegments/
│
├── main.py                  # Aplicación FastAPI
├── model_manager.py         # Carga del modelo entrenado
├── modelbuilder.py          # Script de entrenamiento
│
├── models/
│   └── best_model.pkl       # Modelo final guardado
│
├── templates/
│   └── index.html           # Formulario web
│
├── static/
│   ├── style.css            # Estilos personalizados
│   └── images/
│       └── smartphones.png  # Imagen de fondo
│
├── data/
│   └── smartphone_segments.csv
│
└── requirements.txt
```


## Cómo ejecutar el proyecto localmente

1. Clonar el [repositorio](https://github.com/evelinrkalil13/SmartPhoneSegments.git)
2. Crear el entorno virtual
    ```bash
    python -m venv .venv
    ```
3. Activar el entorno virtual
    ```bash
    .venv\Scripts\activate
    ```
4. Instalar dependencias
    ```bash
    pip install -r requirements.txt
    ```
5. Lanzar aplicación
    ```bash
    uvicorn main:app --reload
    ```
6. Abrir el navegagor y acceder a [http://localhost:8000](http://localhost:8000)

## Uso de la API en Thunder Client o Postman

Además de la interfaz web, la aplicación ofrece un endpoint tipo API para realizar predicciones directamente desde herramientas como Thunder Client, Postman o integraciones externas.

### Endpoint disponible

POST http://localhost:8000/predecir

Este endpoint espera una solicitud en formato JSON, donde cada objeto representa las especificaciones técnicas de un smartphone.

### Ejemplo de cuerpo (body) en formato JSON

Este es un ejemplo de entrada válida. Puedes copiar y pegar directamente en Thunder Client o Postman:
```json
  {
    "price_usd": 699,
    "battery_mah": 5000,
    "ram_gb": 8,
    "storage_gb": 128,
    "camera_mp": 64,
    "screen_size_in": 6.5,
    "weight_g": 185
  }
```
### Ejemplo de respuesta
```json
{
  "message": "Hola, el segmento estimado de tu SmartPhone es:",
  "predicción": "Midrange"
}
```
### Consideraciones

- El cuerpo debe ser una lista de objetos, aunque se envíe un solo smartphone.
- Todos los campos son numéricos y obligatorios.
- Si los datos no están bien estructurados, la API devolverá un error.

## Créditos

Este proyecto fue desarrollado como parte de un curso de Análitica / Machine Learning, con fines académicos.
