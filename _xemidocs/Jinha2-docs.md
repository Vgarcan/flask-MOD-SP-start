# Guía Completa sobre Jinja2 y el Uso de Filtros en Flask

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Instalación](#instalación)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Uso Básico de Jinja2](#uso-básico-de-jinja2)
    - [Sintaxis de Plantillas](#sintaxis-de-plantillas)
    - [Variables](#variables)
    - [Control de Flujo](#control-de-flujo)
5. [Filtros en Jinja2](#filtros-en-jinja2)
    - [Filtros Incorporados](#filtros-incorporados)
    - [Filtros Personalizados](#filtros-personalizados)
6. [Plantillas HTML](#plantillas-html)
    - [index.html](#indexhtml)
7. [Recursos Adicionales](#recursos-adicionales)

## Introducción

Jinja2 es un motor de plantillas para Python que se utiliza ampliamente en aplicaciones Flask para renderizar HTML. Jinja2 permite la separación de la lógica de la presentación y la lógica de la aplicación, proporcionando una forma eficiente de generar contenido dinámico en tus aplicaciones web. Una de las características más poderosas de Jinja2 son los filtros, que permiten modificar la presentación de las variables directamente en las plantillas.

## Instalación

Jinja2 viene integrado con Flask, por lo que no necesitas instalarlo por separado. Sin embargo, debes asegurarte de tener Flask instalado:

```bash
pip install Flask
```

## Estructura del Proyecto

Una estructura de proyecto organizada facilita el mantenimiento y la escalabilidad de tu aplicación Flask. A continuación se muestra una estructura básica del proyecto para trabajar con Jinja2:

```
myapp/
│
├── app.py
├── config.py
├── models.py
├── forms.py
├── templates/
│   ├── index.html
├── requirements.txt
└── migrations/
```

## Uso Básico de Jinja2

### Sintaxis de Plantillas

Jinja2 utiliza una sintaxis de plantillas que permite la inserción de variables y el uso de estructuras de control directamente en los archivos HTML. Las expresiones de Jinja2 están delimitadas por `{% ... %}` para las declaraciones y `{{ ... }}` para las expresiones.

### Variables

Puedes pasar variables desde tu aplicación Flask a tus plantillas Jinja2 y usarlas para renderizar contenido dinámico. Aquí tienes un ejemplo básico:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user = {'username': 'John Doe'}
    return render_template('index.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
```

En este ejemplo, la variable `user` se pasa a la plantilla `index.html`, donde se puede utilizar para mostrar información dinámica.

### Control de Flujo

Jinja2 soporta estructuras de control de flujo como bucles y condicionales, lo que permite una manipulación más avanzada de los datos dentro de las plantillas.

#### Bucles

Los bucles se utilizan para iterar sobre secuencias de datos.

```html
<ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
```

#### Condicionales

Los condicionales permiten mostrar contenido basado en ciertas condiciones.

```html
{% if user %}
    <p>Hello, {{ user.username }}!</p>
{% else %}
    <p>Hello, Guest!</p>
{% endif %}
```

## Filtros en Jinja2

Los filtros en Jinja2 son una forma poderosa de modificar la presentación de las variables directamente en las plantillas. Se aplican utilizando el símbolo de tubería (`|`).

### Filtros Incorporados

Jinja2 incluye una variedad de filtros incorporados que puedes usar directamente en tus plantillas.

#### Ejemplos de Filtros Incorporados

- **`length`**: Devuelve la longitud de una secuencia.
  
  ```html
  <p>Number of items: {{ items|length }}</p>
  ```

- **`upper`**: Convierte una cadena a mayúsculas.
  
  ```html
  <p>{{ user.username|upper }}</p>
  ```

- **`lower`**: Convierte una cadena a minúsculas.
  
  ```html
  <p>{{ user.username|lower }}</p>
  ```

- **`date`**: Formatea una fecha.

  ```html
  <p>{{ post.date|date("Y-m-d") }}</p>
  ```

- **`default`**: Devuelve un valor predeterminado si la variable es `None`.

  ```html
  <p>{{ user.location|default('Unknown') }}</p>
  ```

- **`safe`**: Marca una cadena como segura, permitiendo que el HTML no sea escapado.

  ```html
  <p>{{ user.bio|safe }}</p>
  ```

### Filtros Personalizados

Además de los filtros incorporados, puedes definir tus propios filtros personalizados en Jinja2 para satisfacer necesidades específicas de tu aplicación.

#### Definición de un Filtro Personalizado

Puedes definir un filtro personalizado en tu aplicación Flask y registrarlo para usarlo en tus plantillas.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

@app.route('/')
def index():
    user = {'username': 'John Doe'}
    return render_template('index.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
```

#### Uso de un Filtro Personalizado en Plantilla

Una vez definido y registrado el filtro, puedes usarlo en tus plantillas de la misma manera que usas los filtros incorporados.

```html
<p>{{ user.username|reverse }}</p>
```

## Plantillas HTML

Las plantillas HTML se utilizan para renderizar las páginas web. Flask utiliza Jinja2 como su motor de plantillas por defecto, lo que permite una fácil integración y uso de las características de Jinja2.

### templates/index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Jinja2 with Flask</h1>
    <p>Hello, {{ user.username }}!</p>
    <p>Username in reverse: {{ user.username|reverse }}</p>
</body>
</html>
```

## Recursos Adicionales

Para profundizar más en el uso de Jinja2 y Flask, puedes consultar los siguientes recursos:

- **Documentación de Jinja2**: [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- **Flask Mega-Tutorial by Miguel Grinberg**: [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)
- **Filtros en Jinja2**: [Jinja2 Filters](https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-builtin-filters)
- **Custom Filters in Flask**: [Flask Custom Filters](https://flask.palletsprojects.com/en/1.1.x/templating/#registering-filters)

Esta guía cubre los conceptos básicos de Jinja2 y su uso en Flask, haciendo hincapié en la utilización de filtros para manipular y presentar datos de manera eficiente en tus plantillas HTML. Con estos conocimientos, estarás mejor preparado para desarrollar aplicaciones web dinámicas y mantenibles.