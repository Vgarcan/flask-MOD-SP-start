"""
run.py
El archivo principal de la aplicación Flask.
Inicializa la aplicación y configura las extensiones necesarias.

Uso:
1. Importa la función create_app desde el paquete principal de la aplicación.
2. Inicializa la aplicación llamando a create_app().
3. Ejecuta la aplicación en modo debug si se ejecuta directamente.

Ejemplo:
from flask import Flask
from myapp import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
"""
from flask import Flask
from core import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)