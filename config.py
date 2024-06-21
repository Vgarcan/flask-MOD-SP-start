"""
config.py
Archivo de configuración para la aplicación Flask.
Gestiona las variables de entorno y configura las extensiones.

Uso:
1. Define una clase Config que contiene las configuraciones.
2. Utiliza os.getenv para obtener las variables de entorno.

Ejemplo:
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    MONGO_URI = os.getenv('MONGO_URI')
"""
