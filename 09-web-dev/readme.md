# Web Development with Flask

Flask is a lightweight web framework for Python that is widely used for building web applications. It follows the WSGI standard and provides simplicity and flexibility.

## Deep Dive into Flask

### Installation

```bash
pip install Flask
```

### Basic Flask App

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
```

### Routing

```python
@app.route('/about')
def about():
    return 'About Page'
```

### Templates (Jinja2)

```python
from flask import render_template

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)
```

### Forms

```python
from flask import Flask, render_template, request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Authentication logic (not implemented here)
    return render_template('login.html')
```

### Flask SQLAlchemy (Database Interaction)

```bash
pip install Flask-SQLAlchemy
```

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)

if __name__ == '__main__':
    app.run(debug=True)
```

### Flask RESTful (Building APIs)

```bash
pip install Flask-RESTful
```

```python
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
```

# Templating Engines and MVC Architecture

## Jinja2 Templating Engine

Jinja2 is the default templating engine used by Flask. It allows embedding dynamic content into HTML templates.

### Example Template (profile.html)

```html
<!DOCTYPE html>
<html>
<head>
    <title>User Profile</title>
</head>
<body>
    <h1>Welcome, {{ username }}!</h1>
</body>
</html>
```

## Model-View-Controller (MVC) Architecture

MVC is a design pattern that separates an application into three interconnected components: Model, View, and Controller.

### Model

The model represents the data and business logic of the application. In Flask, SQLAlchemy is often used for database interaction.

### View

The view is responsible for presenting the data to the user. In Flask, templates (HTML files with Jinja2) are used for rendering views.

### Controller

The controller handles user input, processes it, and updates the model and view accordingly. In Flask, the routes and associated functions act as controllers.

The integration of these concepts makes Flask a powerful and extensible framework for web development. It allows developers to build scalable and maintainable web applications with ease.