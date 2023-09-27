class Map:  
    def __init__(self, width, height):  
        self.rooms = [[None for _ in range(width)] for _ in range(height)]  
  
    def add_room(self, room, x, y):  
        self.rooms[y][x] = room  
