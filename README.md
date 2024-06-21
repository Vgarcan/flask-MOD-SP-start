# Proj_Main

Este es un proyecto web basado en Flask que utiliza MongoDB como base de datos. La estructura del proyecto sigue una arquitectura modular que permite añadir y gestionar aplicaciones adicionales de manera sencilla.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
proj_main/
│
├── app1/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
│       └── app1/
│           ├── login.html
│           └── register.html
│
├── proj_main/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   └── static/
│       ├── css/
│       ├── img/
│       └── js/
│
├── .env
├── requirements.txt
└── run.py
```

### Descripción de Archivos y Carpetas Clave

#### `proj_main/__init__.py`
```python
"""
proj_main/__init__.py
Inicializa la aplicación principal de Flask y registra las aplicaciones.

Este archivo configura la aplicación principal de Flask, inicializa las extensiones y
registra las aplicaciones (módulos) que forman parte del proyecto.

Uso:
1. Inicializa las extensiones necesarias (e.g., PyMongo, Flask-Login).
2. Registra los blueprints de las aplicaciones individuales.

Ejemplo:
    from flask import Flask
    from .extensions import mongo, login_manager

    def create_app():
        app = Flask(__name__)
        app.config.from_object('proj_main.config.Config')
        
        # Inicializar extensiones
        mongo.init_app(app)
        login_manager.init_app(app)
        
        # Registrar blueprints
        from app1.views import app1 as app1_bp
        app.register_blueprint(app1_bp, url_prefix='/app1')
        
        return app
"""
```

#### `proj_main/config.py`
```python
"""
proj_main/config.py
Archivo de configuración para la aplicación Flask.

Este archivo define la configuración de la aplicación Flask, incluyendo las variables
de entorno cargadas desde un archivo `.env`.

Uso:
1. Define las clases de configuración necesarias.
2. Carga las variables de entorno usando `python-dotenv`.

Ejemplo:
    import os
    from dotenv import load_dotenv

    load_dotenv()

    class Config:
        SECRET_KEY = os.getenv('SECRET_KEY')
        MONGO_URI = os.getenv('MONGO_URI')
"""
```

#### `proj_main/extensions.py`
```python
"""
proj_main/extensions.py
Inicializa las extensiones utilizadas en la aplicación Flask.

Este archivo se encarga de crear las instancias de las extensiones que serán utilizadas
en la aplicación y que serán inicializadas en `proj_main/__init__.py`.

Uso:
1. Define las instancias de las extensiones necesarias.

Ejemplo:
    from flask_pymongo import PyMongo
    from flask_login import LoginManager

    mongo = PyMongo()
    login_manager = LoginManager()
"""
```

#### `app1/__init__.py`
```python
"""
app1/__init__.py
Inicializa la aplicación `app1`.

Este archivo se encarga de configurar y registrar los componentes específicos de la
aplicación `app1`, como modelos, vistas y formularios.

Uso:
1. Configura los componentes específicos de la aplicación.
2. Registra los blueprints necesarios.

Ejemplo:
    from flask import Blueprint

    app1 = Blueprint('app1', __name__, template_folder='templates', static_folder='static')

    from . import views
"""
```

#### `app1/views.py`
```python
"""
app1/views.py
Define las vistas para la aplicación `app1`.

Este archivo define las rutas y las funciones de vista para `app1` y registra el blueprint
correspondiente. No es necesario registrar el blueprint en `app1/__init__.py` si se hace aquí.

Uso:
1. Define las funciones de vista para las rutas específicas.
2. Registra el blueprint de la aplicación.

Ejemplo:
    from flask import Blueprint, render_template

    app1 = Blueprint('app1', __name__, template_folder='templates', static_folder='static')

    @app1.route('/login')
    def login():
        return render_template('app1/login.html')
"""
```

### Configuración de Variables de Entorno

Para configurar las variables de entorno, crea un archivo `.env` en el directorio raíz del proyecto con el siguiente contenido:

```plaintext
SECRET_KEY=supersecretkey
MONGO_URI=mongodb+srv://username:password@cluster0.mongodb.net/mydatabase
```

### Incluir una Nueva Aplicación

1. **Crea una nueva carpeta para la aplicación:**

   ```bash
   mkdir app2
   cd app2
   touch __init__.py models.py views.py forms.py
   mkdir templates
   mkdir templates/app2
   mkdir static
   ```

2. **Configura la nueva aplicación en `app2/__init__.py`:**

   ```python
   from flask import Blueprint

   app2 = Blueprint('app2', __name__, template_folder='templates', static_folder='static')

   from . import views
   ```

3. **Registra la nueva aplicación en `proj_main/__init__.py`:**

   ```python
   from app2.views import app2 as app2_bp
   app.register_blueprint(app2_bp, url_prefix='/app2')
   ```

### Configuración de Archivos Estáticos

Los archivos estáticos como CSS, imágenes y JavaScript deben almacenarse en la carpeta `static` dentro de `proj_main`. La estructura puede ser la siguiente:

```
proj_main/static/
├── css/
│   └── styles.css
├── img/
│   └── logo.png
└── js/
    └── scripts.js
```

### Ejecutar la Aplicación

1. **Ejecuta la aplicación:**

   ```bash
   python run.py
   ```

2. **Accede a la aplicación en el navegador:**

   ```
   http://127.0.0.1:5000
   ```

### Pruebas

Para ejecutar las pruebas, utiliza el siguiente comando:

```bash
pytest
```

### Contribuciones

Las contribuciones son bienvenidas. Por favor, realiza un fork del repositorio y envía un pull request.

### Licencia

Este proyecto está bajo la Licencia MIT.
