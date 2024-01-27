from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Flask: Building a Simple API
@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify({'message': 'Hello, API!'})

# Consuming an API with Authentication and Error Handling
def consume_api():
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

if __name__ == '__main__':
    # Flask: Run the API server
    app.run(debug=True, port=5000)

    # Consuming an API
    consume_api()
