import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(('localhost', 12345))

# Listen for incoming connections
server_socket.listen()

print("Server is listening for incoming connections...")

# Accept a connection and establish a connection with the client
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

# Receive data from the client
data = client_socket.recv(1024)
print(f"Received data: {data.decode()}")

# Send a response to the client
response = "Hello, client! Thanks for connecting."
client_socket.send(response.encode())

# Close the connection
client_socket.close()
