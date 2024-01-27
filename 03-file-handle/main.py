import os
import shutil
import pickle
import json

# Working with Binary Files

# Writing binary data to a file
binary_data = b'\x48\x65\x6C\x6C\x6F'  # Example binary data (Hello in ASCII)
with open('output.bin', 'wb') as binary_file:
    binary_file.write(binary_data)

# Reading binary data from a file
with open('output.bin', 'rb') as binary_file:
    read_binary_data = binary_file.read()
    print("Read Binary Data:", read_binary_data)


# Using os and shutil for File Operations

# Get current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# List files in the current directory
files_in_directory = os.listdir('.')
print("Files in Directory:", files_in_directory)

# Create a new folder
new_folder_path = 'new_folder'
os.mkdir(new_folder_path)

# Copy a file to the new folder
shutil.copy('output.bin', new_folder_path)


# Serialization and Deserialization with Pickle

# Serialize a Python object to a file using Pickle
data_to_serialize = {'name': 'John', 'age': 30}
with open('data.pickle', 'wb') as pickle_file:
    pickle.dump(data_to_serialize, pickle_file)

# Deserialize the Pickle file
with open('data.pickle', 'rb') as pickle_file:
    deserialized_data_pickle = pickle.load(pickle_file)
    print("Deserialized Data (Pickle):", deserialized_data_pickle)


# Serialization and Deserialization with JSON

# Serialize a Python object to a JSON file
data_to_serialize_json = {'name': 'Jane', 'age': 25}
with open('data.json', 'w') as json_file:
    json.dump(data_to_serialize_json, json_file)

# Deserialize the JSON file
with open('data.json', 'r') as json_file:
    deserialized_data_json = json.load(json_file)
    print("Deserialized Data (JSON):", deserialized_data_json)

# Cleanup: Remove the new folder created
shutil.rmtree(new_folder_path)
