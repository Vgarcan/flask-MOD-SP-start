"""
proj_main/app1/__init__.py
Inicializa el blueprint para las rutas principales de la aplicación.

Uso:
1. Define un blueprint llamado 'app1' para las rutas principales.
2. Importa las vistas relacionadas y las asocia con el blueprint.
3. Inicializa cualquier extensión o configuración específica para el módulo principal.

Ejemplo:
from flask import Blueprint

app1 = Blueprint('app1', __name__, template_folder='templates', static_folder='static')

# Importar vistas relacionadas
from . import views

# Inicializar configuraciones específicas para el módulo principal
def init_app1(app):
    with app.app_context():
        # Código de inicialización específico para el módulo principal
        pass
"""
