# src/api/main.py

import pandas as pd
from fastapi import FastAPI
import mlflow

# Importamos nuestros esquemas y la configuración
from src.api.schemas import InputData, PredictionResponse
from src import config

# 1. Cargar el modelo de MLflow una sola vez al iniciar la API
# Buscamos la última versión del modelo que fue marcada como "Production"
logged_model_uri = f"models:/{config.REGISTERED_MODEL_NAME}@production"
model = mlflow.pyfunc.load_model(logged_model_uri)
print("✅ Modelo cargado exitosamente desde MLflow.")


# 2. Iniciar la aplicación FastAPI
app = FastAPI(
    title="Boston Housing Price Prediction API",
    description="API para predecir precios de viviendas en Boston usando un modelo de ML.",
    version="1.0.0"
)


# 3. Definir el endpoint de predicción
@app.post("/predict", response_model=PredictionResponse)
def predict(input_data: InputData):
    """
    Recibe datos de una vivienda y devuelve una predicción de su precio.
    """
    # Convertir los datos de entrada Pydantic a un DataFrame de Pandas
    # El modelo espera un DataFrame con columnas específicas.
    input_df = pd.DataFrame([input_data.model_dump()])

    # Asegurarse de que el orden de las columnas sea el correcto
    input_df = input_df[config.FEATURES]

    # Realizar la predicción
    prediction = model.predict(input_df)

    # Devolver la predicción en el formato de respuesta definido
    return PredictionResponse(prediction=prediction[0])


# 4. (Opcional) Definir un endpoint raíz para verificar que la API está viva
@app.get("/")
def read_root():
    return {"status": "ok", "message": "API de predicción de precios de Boston funcionando."}
