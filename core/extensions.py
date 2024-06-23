"""
proj_main/extensions.py
Define e inicializa las extensiones utilizadas en la aplicación, como PyMongo y Flask-Login.

Uso:
1. Importa las extensiones necesarias.
2. Inicializa las extensiones sin aplicación para permitir su inicialización tardía.

Ejemplo:
from flask_pymongo import PyMongo
from flask_login import LoginManager

mongo = PyMongo()
login_manager = LoginManager()
"""
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy