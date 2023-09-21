class Player:  
    def __init__(self, _id, name, password):
        self._id = _id
        self.name = name
        self.password = password
        
    def to_dict(self):  
        return {  
            "_id": self._id,  
            "name": self.name,  
            "password": self.password  
        }  
    
    # This static method creates a new Player instance from a dictionary.  
    @staticmethod  
    def from_dict(data):  
        return Player(data["_id"], data["name"], data["password"]) 