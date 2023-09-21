from Database.Models.player import Player


class ConnectedPlayer:  
    def __init__(self, socket, player):
        self.socket = socket
        self.player = player
