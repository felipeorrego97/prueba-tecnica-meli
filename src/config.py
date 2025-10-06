
# Ruta data
DATA_PATH = "data/HousingData.csv"

# variables del modelo
FEATURES = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM',
            'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']

# variable objetivo
TARGET = 'MEDV'

# division de datos
TEST_SIZE = 0.2
RANDOM_STATE = 42

# configuracion MLflow
MLFLOW_EXPERIMENT_NAME = "boston-house-pricing"
MLFLOW_RUN_NAME = "random_forest_regressor"
REGISTERED_MODEL_NAME = "BostonPricePredictor"
