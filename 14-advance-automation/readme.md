# Advanced Automation in Python

Automation in Python can be extended to more complex scenarios, including integration with external systems and APIs. Below are examples that showcase building complex automation scripts and integrating with external systems.

## Complex Automation Script

### Example: Automated File Management

```python
import os
import shutil
import glob

def organize_files(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get all files in the source directory
    files = glob.glob(os.path.join(source_dir, '*'))

    # Move files to the destination directory based on file extension
    for file_path in files:
        _, file_name = os.path.split(file_path)
        file_extension = file_name.split('.')[-1].lower()
        
        destination_folder = os.path.join(destination_dir, file_extension)
        
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        destination_path = os.path.join(destination_folder, file_name)

        shutil.move(file_path, destination_path)
        print(f"Moved {file_name} to {destination_folder}")

if __name__ == '__main__':
    source_directory = '/path/to/source'
    destination_directory = '/path/to/destination'

    organize_files(source_directory, destination_directory)
```

This script organizes files from a source directory into folders based on their file extensions in a destination directory. It demonstrates file manipulation and organization, showcasing more complex automation.

## Integration with External Systems and APIs

### Example: Sending HTTP Requests using `requests`

```python
import requests

def fetch_data_from_api(api_url):
    try:
        # Send GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Process the JSON response
            data = response.json()
            return data
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
        return None

if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com/todos/1'

    # Fetch data from the API
    api_data = fetch_data_from_api(api_url)

    if api_data:
        print("API Data:")
        print(api_data)
```

This script uses the `requests` library to send an HTTP GET request to a sample API (`jsonplaceholder.typicode.com`). It demonstrates how to fetch and process data from an external API, showcasing integration capabilities.

These examples demonstrate more complex automation scenarios, including file management and interaction with external systems using Python. Adopting such practices enhances the versatility and power of automation scripts.