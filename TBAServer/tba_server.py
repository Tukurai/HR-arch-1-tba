# tba-server.py  
  
import sys  
import socket  
import selectors
from Models.connected_player import ConnectedPlayer
from Database.data_client import DataClient
from Database.Models.player import Player  
  
# Importing ClientData class from client_data module.  
from client_data import ClientData  
  
# Creating a default selector.  
selector = selectors.DefaultSelector()

# Database client
database = None

# Connected players
connected_players = {}

# Function to accept a connection.  
def accept_wrapper(sock):  
    connection, address = sock.accept()  # Socket should be ready to read  
    print(f"Accepted connection from {address[0]}:{address[1]}")  
  
    player = ConnectedPlayer(sock, None)  
    connected_players[f"{address[0]}:{address[1]}"] = player  
  
    # Making the connection non-blocking.  
    connection.setblocking(False)  
  
    # Creating a ClientData object to keep track of the connection data.  
    data = ClientData(address=address, incoming_bytes=b"", outgoing_bytes=b"INPUT|Welcome to TBA, Enter your username:")  
  
    # Registering the connection for both read and write events.  
    events = selectors.EVENT_READ | selectors.EVENT_WRITE  
    selector.register(connection, events, data=data)  
  
# Function to service a connection.  
def service_connection(key, mask):  
    socket = key.fileobj  
    data = key.data  
    player_data = connected_players[f"{data.address[0]}:{data.address[1]}"]  
  
    # If there is data to read  
    if mask & selectors.EVENT_READ:  
        received_data = None
        try:
            received_data = socket .recv(1024)  # Socket should be ready to read  

            if not received_data:
                raise ConnectionResetError()

        except ConnectionResetError:
            print(f"Closing connection to {data.address}")  
            selector.unregister(socket)  
            socket.close() 
            return 
        

        if received_data.decode() != "CONNECT":
            if player_data.player is None:  
                
                player_name = received_data.decode()
                if not any(player_name in connection.player.name for connection in connected_players.values() if connection.player is not None):
                    player_data.player = Player(None, player_name, None)

                    mongo_player = database.load_single("players", {'name': player_data.player.name})

                    if mongo_player is not None:
                        data.outgoing_bytes += b"INPUT|Enter password:"  
                    else:
                        data.outgoing_bytes += b"INPUT|Create a password:"

                else:
                    data.outgoing_bytes += b"INPUT|Already connected elsewhere! Enter a different username:"  
                    player_data.player = None
                
            elif player_data.player.password is None:  

                player_data.player.password = received_data.decode()  
                
                mongo_player = Player.from_dict(database.load_single("players", {'name': player_data.player.name}))

                if mongo_player is not None:
                    if mongo_player.password == player_data.player.password:
                        data.outgoing_bytes += b"INPUT|Welcome to TBA"
                    else:
                        data.outgoing_bytes += b"INPUT|Wrong password, starting over, enter your username:"
                        player_data.player = None
                else:
                    database.save("players", player_data.player.to_dict())
                    data.outgoing_bytes += b"INPUT|Username registered, welcome to TBA"
  
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

# Connect to MongoDB
database = DataClient()
  
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
