# src/pipeline/pipeline.py

from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Usaremos un RandomForestRegressor. Es un modelo robusto que generalmente
# da buenos resultados sin necesidad de un ajuste de hiperparámetros exhaustivo.
# El random_state es para asegurar la reproducibilidad del modelo.
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Creamos el pipeline de ML


def create_pipeline() -> Pipeline:
    """
    Crea y devuelve un pipeline de Scikit-learn que:
    1. Imputa valores faltantes con la media.
    2. Escala las características.
    3. Entrena un modelo RandomForestRegressor.
    """
    price_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler()),
        ('model', model)
    ])

    return price_pipeline
