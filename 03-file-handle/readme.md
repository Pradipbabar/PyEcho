# Advanced File Handling

## Working with Binary Files

### Reading Binary File

```python
# Read binary data from a file
with open('binary_data.bin', 'rb') as file:
    binary_content = file.read()
    print("Binary Content:", binary_content)
```

### Writing to Binary File

```python
# Write binary data to a file
binary_data = b'\x48\x65\x6C\x6C\x6F'  # Example binary data (Hello in ASCII)
with open('output.bin', 'wb') as file:
    file.write(binary_data)
```

## Using os and shutil for File Operations

### Using os Module

```python
import os

# Get current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# List files in a directory
files_in_directory = os.listdir('.')
print("Files in Directory:", files_in_directory)
```

### Using shutil Module

```python
import shutil

# Copy a file to a new location
shutil.copy('source_file.txt', 'destination_folder/')

# Move a file to a new location
shutil.move('source_file.txt', 'new_location/')
```

## Serialization and Deserialization

### Using Pickle for Serialization

```python
import pickle

# Serialize a Python object to a file
data_to_serialize = {'name': 'John', 'age': 30}
with open('data.pickle', 'wb') as file:
    pickle.dump(data_to_serialize, file)
```

### Using Pickle for Deserialization

```python
# Deserialize a Python object from a file
with open('data.pickle', 'rb') as file:
    deserialized_data = pickle.load(file)
    print("Deserialized Data:", deserialized_data)
```

### Using JSON for Serialization

```python
import json

# Serialize a Python object to a JSON file
data_to_serialize = {'name': 'Jane', 'age': 25}
with open('data.json', 'w') as file:
    json.dump(data_to_serialize, file)
```

### Using JSON for Deserialization

```python
# Deserialize a Python object from a JSON file
with open('data.json', 'r') as file:
    deserialized_data_json = json.load(file)
    print("Deserialized Data (JSON):", deserialized_data_json)
```

These examples demonstrate advanced file handling techniques in Python, including working with binary files, using the `os` and `shutil` modules for file operations, and serialization/deserialization using both Pickle and JSON.