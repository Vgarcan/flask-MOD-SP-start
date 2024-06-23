"""
proj_main/app1/views.py
Contiene las vistas y rutas relacionadas con los usuarios, como registro y autenticación.

Uso:
1. Define un blueprint para las rutas relacionadas con usuarios.
2. Implementa las vistas para el registro, inicio de sesión y cierre de sesión.
3. Utiliza formularios de WTForms para manejar la entrada del usuario.

Ejemplo:
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from .forms import RegistrationForm, LoginForm
from .models import User

app1 = Blueprint('app1', __name__, template_folder='templates', static_folder='static')

@app1.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        mongo.db.app1.insert_one({'username': new_user.username, 'password': new_user.password})
        flash('Registration successful!', 'success')
        return redirect(url_for('app1.login'))
    return render_template('register.html', form=form)

@app1.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get(form.username.data)
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('main.index'))
        flash('Invalid credentials', 'danger')
    return render_template('login.html', form=form)

@app1.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
"""
