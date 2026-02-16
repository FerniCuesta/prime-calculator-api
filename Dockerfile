# Usamos la versión de Python que tenemos en local y en el CI
FROM python:3.12-slim

# Evita que Python genere archivos .pyc y permite ver logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código fuente
COPY . .

# Exponemos el puerto (suponiendo que usas FastAPI/Uvicorn más adelante)
EXPOSE 8000

# Comando para arrancar (simulado por ahora)
CMD ["python", "-m", "src.backend.calculator"]