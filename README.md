### Instrucciones de Uso

1.  **Clonar el repositorio:**
    crea una carpeta en la que se va a clonar el repositorio, mediante el terminal llega a esa dirección y ejecuta:
    git clone https://github.com/felipeorrego97/prueba-tecnica-meli.git
    

2.  **Entrenar el modelo:**
    Este comando usará Docker Compose para construir la imagen y ejecutar el script de entrenamiento en un contenedor. Creará la carpeta `mlruns` con el modelo y los resultados.
    docker-compose run --rm training


3.  **Promover el modelo a producción:**
    * Inicia la interfaz de MLflow con el siguiente comando:
        mlflow ui

    * Abre tu navegador en `http://127.0.0.1:5000`.
    * Ve a "Models" > "BostonPricePredictor" > "Version 1".
    * Usa el botón "Promote model" para asignarle el alias `production`.
    en esta interfas puedes revisar las métricas del modelo

4.  **Levantar la API de predicción:**
    para levantar el api ejecuta el siguiente comando:
    docker-compose up api
    
    La API ahora estará corriendo y será accesible en `http://127.0.0.1:8000`.

5.  **Probar la API:**
    Puedes usar la documentación interactiva en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para enviar peticiones de prueba.
    el api tiene dos métodos. el Get que devuelve una respuesta genérica de respuesta del api y el post que devuelve la predicción de precio según las variables que enviemos.

    un ejemplo del json para probar el api es el siguiente: 
    {
  "CRIM": 0,
  "ZN": 0,
  "INDUS": 0,
  "CHAS": 0,
  "NOX": 0,
  "RM": 0,
  "AGE": 0,
  "DIS": 0,
  "RAD": 0,
  "TAX": 0,
  "PTRATIO": 0,
  "B": 0,
  "LSTAT": 0
}

este es el significado de cada variable

Características de la Zona y el Entorno

CRIM: Tasa de criminalidad per cápita del suburbio. Un valor más alto significa más crimen.

ZN: Porcentaje de terreno residencial dividido en lotes de más de 25,000 pies cuadrados (unos 2,300 m²). Indica si es una zona de casas grandes y espaciadas.

INDUS: Porcentaje de terreno industrial no destinado a comercios. Mide qué tan industrializada es la zona.

CHAS: Proximidad al río Charles. Es una variable binaria: 1 si el suburbio bordea el río, 0 si no.

NOX: Concentración de óxidos de nitrógeno (en partes por 10 millones). Es un indicador de la calidad del aire y la contaminación.

Características de las Propiedades

RM: Número promedio de habitaciones por vivienda. Es una de las variables más influyentes; más habitaciones suele implicar un precio más alto.

AGE: Edad de las viviendas. Proporción de viviendas ocupadas por sus dueños que fueron construidas antes de 1940.

Factores de Accesibilidad y Socioeconómicos
DIS: Distancia ponderada a los cinco principales centros de empleo de Boston. Un valor más bajo significa que está más cerca de las zonas de trabajo.

RAD: Índice de accesibilidad a las autopistas radiales. Mide qué tan bien conectado está el suburbio.

TAX: Tasa de impuesto a la propiedad por cada $10,000 de valor.

PTRATIO: Ratio de alumnos por profesor en las escuelas del suburbio. Es un indicador de la calidad educativa.

LSTAT: Porcentaje de la población considerada de "estatus bajo". Mide el nivel socioeconómico del área.

Variable Histórica/Problemática

B: Esta es una variable más compleja y éticamente problemática, calculada en base a la proporción de residentes afroamericanos en la ciudad. 




Uso de herramientas de IA

La inteligencia artificial ha permitido en los últimos años agilizar el trabajo de los desarrolladores. Es por esto que es una herramienta muy útil a la hora de trabajar culquier solución
En este caso la IA se utilizó principalmente para tener un boceto de la solución y se fue moldeando para encontrar la mejor opción para cada código siempre siendo muy crítico con las soluciones que suministraba y apalancándonos del conocimiento que se tiene validar si las respuestas que se dan son las más adecuadas
