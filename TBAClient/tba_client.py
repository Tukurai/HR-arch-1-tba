# tba-client.py  
  
import sys  
import socket  
import selectors  
import types  

from connection_data import ConnectionData
  
# Create a default selector  
selector = selectors.DefaultSelector()  
  
# Function to start a connection  
def start_connection(host, port, message):  
    server_address = (host, port)  
    print(f"Starting connection to {server_address}")  
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.setblocking(False)  
    sock.connect_ex(server_address)  
  
    # Register events to monitor  
    events = selectors.EVENT_READ | selectors.EVENT_WRITE  
  
    # Create a namespace to hold the connection data  
    data = ConnectionData(  
        connection_name = socket.gethostname(),  
        message_total_length = len(message),  
        received_total = 0,  
        messages = list(),  
        outgoing_bytes = message,  
    )  
  
    # Register the socket with the selector to monitor events  
    selector.register(sock, events, data=data)  
  
  
# Function to handle connections  
def service_connection(key, mask):  
    sock = key.fileobj  
    data = key.data  
  
    # If there is data to read  
    if mask & selectors.EVENT_READ:  
        recv_data = sock.recv(1024)  # Should be ready to read  
        if recv_data:  
            # print(f"DEBUG: Received {recv_data!r} from connection {data.connection_name}")  

            message_data = recv_data.decode().split('|')
            if len(message_data) > 1: # message has a command type.
                match message_data[0]:
                    case 'INPUT':
                        data.outgoing_bytes = input(f"{message_data[1]}").encode()  
            else:
                print(f"{recv_data!r}")  
            data.received_total += len(recv_data)  
  
        # If no data received or all data sent has been received  
        if not recv_data or data.received_total == data.message_total_length:  
            # Ask for a new message  
            data.outgoing_bytes = input("Enter message or 'quit' to exit: ").encode()  
  
            # If user wants to quit, close the connection  
            if data.outgoing_bytes.decode() == 'quit':  
                print(f"Closing connection...")  
                selector.unregister(sock)  
                sock.close() 
                return
  
            # Else, reset totals for the new message  
            else:  
                data.message_total_length = len(data.outgoing_bytes)  
                data.received_total = 0  
  
    # If there is data to write  
    if mask & selectors.EVENT_WRITE:  
        if data.outgoing_bytes:
            sent = sock.send(data.outgoing_bytes)  # Should be ready to write  
            data.outgoing_bytes = data.outgoing_bytes[sent:]  
  
  
if len(sys.argv) != 3:  
    print(f"Usage: {sys.argv[0]} <host> <port>")  
    sys.exit(1)  
  
host, port = sys.argv[1:3]  
message = "CONNECT".encode()  
  
# Start a connection with the initial message  
start_connection(host, int(port), message)  
  
try:  
    while True:  
        # Get events and for each one, handle the connection  
        events = selector.select(timeout=1)  
        if events:  
            for key, mask in events:  
                service_connection(key, mask)  
  
        # If no sockets are being monitored, break the loop  
        if not selector.get_map():  
            break  
  
# Allow the program to exit on Ctrl+C  
except KeyboardInterrupt:  
    print("Caught keyboard interrupt, exiting")  
  
# Always make sure the selector is closed before exiting  
finally:  
    selector.close()  
