class ConnectionData:  
    def __init__(self, connection_name, message_total_length, received_total, messages, outgoing_bytes):  
        self.connection_name = connection_name  
        self.message_total_length = message_total_length  
        self.received_total = received_total  
        self.messages = messages  
        self.outgoing_bytes = outgoing_bytes 