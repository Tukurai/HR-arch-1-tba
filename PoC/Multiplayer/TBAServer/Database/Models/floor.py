
class Floor:  
    def __init__(self, _id, name, rooms=None):
        self._id = _id
        self.name = name
        self.rooms = rooms if rooms is not None else []  

    def add_room(self, room):  
        self.rooms.append(room)  

    # This method converts the Floor instance to a dictionary.  
    def to_dict(self):  
        # Store only the _id of each Room instance in rooms.  
        room_ids = [room._id for room in self.rooms]  
        return {  
            "_id": self._id,  
            "name": self.name,  
            "rooms": room_ids  
        }  
    