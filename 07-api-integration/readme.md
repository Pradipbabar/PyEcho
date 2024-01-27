# Advanced API Interaction

## Building APIs with Flask or Django

### Flask Example

Flask is a lightweight web framework for building web applications and APIs in Python.

#### Example: Creating a Simple API with Flask

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify({'message': 'Hello, API!'})

if __name__ == '__main__':
    app.run(debug=True)
```

1. Install Flask: `pip install Flask`
2. Run the Flask app: `python app.py`

The API will be accessible at `http://localhost:5000/api/greet`.

### Django Example

Django is a high-level web framework that includes built-in tools for creating APIs.

#### Example: Creating a Simple API with Django

1. Create a Django project: `django-admin startproject myproject`
2. Create a Django app: `python manage.py startapp myapp`
3. Define views in `views.py`:

   ```python
   from django.http import JsonResponse

   def greet(request):
       return JsonResponse({'message': 'Hello, API!'})
   ```

4. Configure URLs in `urls.py`:

   ```python
   from django.urls import path
   from .views import greet

   urlpatterns = [
       path('api/greet', greet, name='greet'),
   ]
   ```

5. Run the Django development server: `python manage.py runserver`

The API will be accessible at `http://localhost:8000/api/greet`.

## Consuming APIs with Authentication and Error Handling

### Example: Consuming a Mock API with Requests

```python
import requests

# Replace 'your_api_key' with a valid API key
api_key = 'your_api_key'
api_url = 'https://api.example.com/data'

headers = {'Authorization': f'Bearer {api_key}'}

try:
    response = requests.get(api_url, headers=headers)

    # Check for successful response
    response.raise_for_status()

    # Process the JSON response
    data = response.json()
    print(data)

except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
except requests.exceptions.RequestException as err:
    print(f"Request Exception: {err}")
```

This example uses the `requests` library to consume a mock API. It includes authentication using an API key and error handling to manage potential issues during the API request.

Make sure to replace 'your_api_key' with a valid API key from the API provider.

These examples showcase building APIs with Flask or Django and consuming APIs with authentication and error handling using the `requests` library. Understanding both sides of API interaction is crucial for developing robust and reliable applications.