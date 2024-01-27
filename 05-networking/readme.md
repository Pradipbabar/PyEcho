# Explore Networking with Python

## Socket Programming for Network Communication

Socket programming is a fundamental aspect of networking, allowing communication between devices over a network using sockets. Python provides the `socket` module to facilitate socket programming.

### Example: Creating a Simple Server and Client

#### Server (server.py)

```python
import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(('localhost', 12345))

# Listen for incoming connections
server_socket.listen()

# Accept a connection and establish a connection with the client
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

# Send data to the client
client_socket.send(b"Hello, client!")

# Close the connection
client_socket.close()
```

#### Client (client.py)

```python
import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 12345))

# Receive data from the server
data = client_socket.recv(1024)
print("Received data:", data.decode())

# Close the connection
client_socket.close()
```

This example demonstrates a simple server that binds to a specific address and port, listens for incoming connections, and sends a message to the connected client. The client connects to the server, receives the message, and closes the connection.

## Understanding HTTP and Creating Simple Servers

HTTP (Hypertext Transfer Protocol) is the foundation of data communication on the web. Python's `http.server` module provides a basic HTTP server for serving files and handling HTTP requests.

### Example: Creating a Simple HTTP Server

```python
# Using the http.server module (Python 3.x)
# Open a terminal and navigate to the directory you want to serve
# Run the following command: python -m http.server

# Alternatively, for Python 2.x
# python -m SimpleHTTPServer
```

This command starts a simple HTTP server on port 8000 by default. You can access the served files by navigating to `http://localhost:8000` in your web browser.

These examples introduce the basics of socket programming for network communication, as well as creating a simple HTTP server using Python. Building on these fundamentals, you can explore more advanced networking concepts and implement complex network applications.