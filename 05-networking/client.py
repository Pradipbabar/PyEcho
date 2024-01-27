import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 12345))

# Send data to the server
message = "Hello, server! How are you?"
client_socket.send(message.encode())

# Receive a response from the server
response = client_socket.recv(1024)
print(f"Server response: {response.decode()}")

# Close the connection
client_socket.close()
