# main.py
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from model_manager import load_model
import pandas as pd

from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def form_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/clasificar_segmento", response_class=HTMLResponse)
async def clasificar_segmento(
    request: Request,
    price_usd: int = Form(...),
    battery_mah: int = Form(...),
    ram_gb: int = Form(...),
    storage_gb: int = Form(...),
    camera_mp: int = Form(...),
    screen_size_in: float = Form(...),
    weight_g: int = Form(...)
):
    model = load_model("models/best_model.pkl")
    df = pd.DataFrame({
        "price_usd": [price_usd],
        "battery_mah": [battery_mah],
        "ram_gb": [ram_gb],
        "storage_gb": [storage_gb],
        "camera_mp": [camera_mp],
        "screen_size_in": [screen_size_in],
        "weight_g": [weight_g]
    })

    prediction = model.predict(df)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": prediction[0]
        }
    )
