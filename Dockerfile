# Usa una imagen base de Python
FROM python:3.9

# Copia los archivos de la app
WORKDIR /app
COPY app.py /app

# Instala Flask
RUN pip install Flask

# Expone el puerto 5000 y define el comando para iniciar la app
EXPOSE 5000
CMD ["python", "app.py"]
