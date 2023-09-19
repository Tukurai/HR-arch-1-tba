# tba-server.py  
  
import sys  
import socket  
import selectors  
  
# Importing ClientData class from client_data module.  
from client_data import ClientData  
  
# Creating a default selector.  
selector = selectors.DefaultSelector()  
  
# Function to accept a connection.  
def accept_wrapper(sock):  
    connection, address = sock.accept()  # Socket should be ready to read  
    print(f"Accepted connection from {address}")  
  
    # Making the connection non-blocking.  
    connection.setblocking(False)  
  
    # Creating a ClientData object to keep track of the connection data.  
    data = ClientData(address=address, incoming_bytes=b"", outgoing_bytes=b"")  
  
    # Registering the connection for both read and write events.  
    events = selectors.EVENT_READ | selectors.EVENT_WRITE  
    selector.register(connection, events, data=data)  
  
# Function to service a connection.  
def service_connection(key, mask):  
    socket = key.fileobj  
    data = key.data  
  
    # If there is data to read  
    if mask & selectors.EVENT_READ:  
        recieved_data = socket.recv(1024)  # Socket should be ready to read  
        if recieved_data:  
            # Adding received data to outgoing data for echoing  
            data.outgoing_bytes += recieved_data  
        else:  
            # If no data received, closing the connection.  
            print(f"Closing connection to {data.address}")  
            selector.unregister(socket)  
            socket.close()  
  
    # If there is data to write  
    if mask & selectors.EVENT_WRITE:  
        if data.outgoing_bytes:  
            print(f"Echoing {data.outgoing_bytes!r} to {data.address}")  
            sent = socket.send(data.outgoing_bytes)  # Socket should be ready to write  
            data.outgoing_bytes = data.outgoing_bytes[sent:]  
  
# If we do not pass the proper arguments when running the server, show the proper way to call the file.  
if len(sys.argv) != 3:  
    print(f"Usage: {sys.argv[0]} <host> <port>")  
    sys.exit(1)  
  
server_host, server_port = sys.argv[1], int(sys.argv[2])  
  
# Creating a listening socket.  
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
server_socket.bind((server_host, server_port))  
  
# Listening for connections.  
server_socket.listen()  
print(f"Listening on {(server_host, server_port)}")  
  
# Making the socket non-blocking.  
server_socket.setblocking(False)  
  
# Registering the server socket to monitor for read event.  
selector.register(server_socket, selectors.EVENT_READ, data=None)  
  
# Main event loop.  
try:  
    while True:  
        events = selector.select(timeout=None)  
        for key, mask in events:  
            # If key.data is None, that means it's a server socket event, and we need to accept the connection.  
            if key.data is None:  
                accept_wrapper(key.fileobj)  
            else:  
                # Otherwise, it's a client socket event, and we need to handle the client connection.  
                service_connection(key, mask)  
except KeyboardInterrupt:  
    print("Caught keyboard interrupt, exiting")  
finally:  
    selector.close()  
