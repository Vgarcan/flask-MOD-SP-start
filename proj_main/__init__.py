"""
proj_app1/__init__.py
Inicializa la aplicación Flask, registra blueprints y extensiones.

Uso:
1. Define una función create_app para inicializar la aplicación.
2. Configura la aplicación con las configuraciones desde config.Config.
3. Inicializa las extensiones como PyMongo y Flask-Login.
4. Registra los blueprints para organizar las rutas de la aplicación.

Ejemplo:
from flask import Flask
from .extensions import mongo, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Inicializar las extensiones
    mongo.init_app(app)
    login_manager.init_app(app)
    
    # Registrar blueprints
    from .app1.views import app1 as app1_bp
    app.register_blueprint(app1_bp, url_prefix='/')

    from .app2.views import app2 as app2_bp
    app.register_blueprint(app2_bp, url_prefix='/app2')

    from .app3.views import app3 as app3_bp
    app.register_blueprint(app3_bp, url_prefix='/app3')

    return app
"""
