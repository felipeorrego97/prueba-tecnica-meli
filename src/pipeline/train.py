# src/pipeline/train.py

import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

# Importamos nuestras configuraciones y el creador de pipeline
from src import config
from src.pipeline import pipeline


def run_training():
    """Función principal para ejecutar el entrenamiento del modelo."""

    print("--- Iniciando el entrenamiento ---")

    # 1. Cargar datos
    print(f"Cargando datos desde: {config.DATA_PATH}")
    data = pd.read_csv(config.DATA_PATH)

    # 2. Dividir en set de entrenamiento y prueba
    X = data[config.FEATURES]
    y = data[config.TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=config.TEST_SIZE, random_state=config.RANDOM_STATE
    )
    print("Datos divididos en entrenamiento y prueba.")

    # 3. Configurar y empezar el experimento de MLflow
    mlflow.set_experiment(config.MLFLOW_EXPERIMENT_NAME)

    with mlflow.start_run(run_name=config.MLFLOW_RUN_NAME) as run:
        print(f"Iniciando run de MLflow: {run.info.run_name}")

        # Log de parámetros
        mlflow.log_param("test_size", config.TEST_SIZE)
        mlflow.log_param("random_state", config.RANDOM_STATE)

        # 4. Crear y entrenar el pipeline
        price_pipeline = pipeline.create_pipeline()
        print("Entrenando el pipeline...")
        price_pipeline.fit(X_train, y_train)

        # 5. Evaluar el modelo
        print("Evaluando el modelo...")
        predictions = price_pipeline.predict(X_test)

        # Calcular métricas
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        mae = mean_absolute_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        print(f"  RMSE: {rmse:.4f}")
        print(f"  MAE: {mae:.4f}")
        print(f"  R2 Score: {r2:.4f}")

        # 6. Registrar métricas en MLflow
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2_score", r2)

        # 7. Registrar el modelo (pipeline completo) en MLflow
        print("Registrando el modelo en MLflow...")
        mlflow.sklearn.log_model(
            sk_model=price_pipeline,
            artifact_path="model",
            registered_model_name=config.REGISTERED_MODEL_NAME
        )

        print(f"Modelo registrado como: {config.REGISTERED_MODEL_NAME}")
        print("--- Entrenamiento finalizado exitosamente ---")


if __name__ == "__main__":
    run_training()
