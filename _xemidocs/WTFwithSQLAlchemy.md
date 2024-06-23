# Guía para Crear Formularios en Flask-WTF y Flask-SQLAlchemy

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Instalación](#instalación)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Configuración](#configuración)
    - [config.py](#configpy)
    - [app.py](#apppy)
5. [Definición de Modelos](#definición-de-modelos)
    - [models.py](#modelspy)
6. [Creación de Formularios](#creación-de-formularios)
    - [forms.py](#formspy)
7. [Plantillas HTML](#plantillas-html)
    - [home.html](#templateshomehtml)
    - [register.html](#templatesregisterhtml)
8. [Rutas y Vistas](#rutas-y-vistas)
    - [app.py](#apppy-1)
9. [Recursos Adicionales](#recursos-adicionales)

## Introducción

Flask-WTF es una extensión para Flask que simplifica la creación y validación de formularios web. Combina el poder de Flask con WTForms, una biblioteca flexible y extensible para manejar formularios en Python. Flask-SQLAlchemy, por otro lado, es una extensión que añade soporte para SQLAlchemy a Flask, proporcionando una interfaz de ORM (Object-Relational Mapping) que facilita la interacción con bases de datos relacionales.

## Instalación

Para comenzar a usar Flask-WTF y Flask-SQLAlchemy, primero necesitas instalarlos usando `pip`:

```bash
pip install Flask-WTF Flask-SQLAlchemy
```

## Estructura del Proyecto

Una estructura de proyecto organizada es fundamental para mantener un código limpio y fácil de mantener. Aquí tienes una estructura recomendada para un proyecto que utiliza Flask-WTF y Flask-SQLAlchemy:

```
myapp/
│
├── app.py
├── config.py
├── models.py
├── forms.py
├── templates/
│   ├── home.html
│   ├── register.html
├── requirements.txt
└── migrations/
```

## Configuración

### config.py

El archivo `config.py` contiene la configuración de la aplicación, incluyendo la configuración de la base de datos y la clave secreta necesaria para la protección CSRF (Cross-Site Request Forgery).

```python
import os

class Config:
    SECRET_KEY = 'your_secret_key'  # Necesario para CSRF protection
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### app.py

El archivo `app.py` es el punto de entrada de tu aplicación Flask. Aquí configuras Flask-SQLAlchemy y Flask-WTF.

```python
from flask import Flask, render_template, url_for, flash, redirect
from config import Config
from models import db, User
from forms import RegistrationForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
```

## Definición de Modelos

### models.py

Define tus modelos utilizando SQLAlchemy. Los modelos representan las tablas en tu base de datos.

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
```

## Creación de Formularios

### forms.py

Define tus formularios utilizando Flask-WTF. Aquí es donde especificas los campos del formulario y las validaciones necesarias.

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
```

## Plantillas HTML

Las plantillas HTML se utilizan para renderizar las páginas web. Flask utiliza Jinja2 como su motor de plantillas por defecto.

### templates/home.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Home Page</h1>
    <a href="{{ url_for('register') }}">Register</a>
</body>
</html>
```

### templates/register.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST" action="">
        {{ form.hidden_tag() }}
        <div>
            {{ form.username.label }} {{ form.username(size=32) }}
        </div>
        <div>
            {{ form.email.label }} {{ form.email(size=32) }}
        </div>
        <div>
            {{ form.password.label }} {{ form.password(size=32) }}
        </div>
        <div>
            {{ form.confirm_password.label }} {{ form.confirm_password(size=32) }}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
</body>
</html>
```

## Rutas y Vistas

### app.py

Las rutas y vistas manejan la lógica de tu aplicación, incluyendo la presentación de formularios y el manejo de datos enviados por el usuario.

```python
from flask import Flask, render_template, url_for, flash, redirect
from config import Config
from models import db, User
from forms import RegistrationForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
```

## Recursos Adicionales

- **Flask-WTF Documentation**: [Flask-WTF Documentation](https://flask-wtf.readthedocs.io/en/stable/)
- **Flask-SQLAlchemy Documentation**: [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)
- **Flask Mega-Tutorial by Miguel Grinberg**: [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)
