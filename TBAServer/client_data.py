class ClientData:  
    def __init__(self, address, incoming_bytes, outgoing_bytes):  
        self.address = address  
        self.incoming_bytes = incoming_bytes  
        self.outgoing_bytes = outgoing_bytes