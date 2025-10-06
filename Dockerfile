# ----- Fase 1: Base de la Imagen -----
# Usamos una imagen oficial de Python. La etiqueta "slim" significa que es una
# versión ligera, lo que resulta en una imagen final más pequeña.
FROM python:3.12-slim

# ----- Fase 2: Configuración del Entorno -----
# Establecemos el directorio de trabajo dentro del contenedor.
# Todos los comandos siguientes se ejecutarán desde esta ruta.
WORKDIR /app

# ----- Fase 3: Instalación de Dependencias -----
# Copiamos solo el archivo de requerimientos primero. Esto es una optimización.
# Docker guarda en caché cada paso. Si no cambiamos requirements.txt,
# no volverá a instalar las dependencias, haciendo las construcciones más rápidas.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ----- Fase 4: Copia del Código de la Aplicación -----
# Ahora copiamos el código fuente de nuestra aplicación al contenedor.
COPY ./src ./src

# ----- Fase 5: Exposición del Puerto y Comando de Ejecución -----
# Le decimos a Docker que el contenedor escuchará en el puerto 8000.
EXPOSE 8000

# Este es el comando que se ejecutará cuando el contenedor se inicie.
# Usamos 0.0.0.0 para que la API sea accesible desde fuera del contenedor.
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]