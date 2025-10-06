# src/api/schemas.py

from pydantic import BaseModel

# Este esquema define la estructura de los datos de entrada para la predicción.
# FastAPI usará esto para validar que la petición entrante tiene los datos correctos.


class InputData(BaseModel):
    CRIM: float
    ZN: float
    INDUS: float
    CHAS: int
    NOX: float
    RM: float
    AGE: float
    DIS: float
    RAD: int
    TAX: float
    PTRATIO: float
    B: float
    LSTAT: float

# Este esquema define la estructura de la respuesta de la API.


class PredictionResponse(BaseModel):
    prediction: float
