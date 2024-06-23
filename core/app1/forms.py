"""
proj_main/app1/forms.py
Define los formularios de usuario utilizando WTForms.

Uso:
1. Importa FlaskForm desde WTForms.
2. Define los campos del formulario para el registro y el inicio de sesión.
3. Implementa validaciones personalizadas según sea necesario.

Ejemplo:
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
"""
