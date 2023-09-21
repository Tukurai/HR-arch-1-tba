class Planet:  
    def __init__(self, _id, name, fortresses=None):
        self._id = _id
        self.name = name
        self.fortresses = fortresses if fortresses is not None else []  

    def add_fortress(self, fortress):  
        self.fortresses.append(fortress)  
        
    # This method converts the Planet instance to a dictionary.  
    def to_dict(self):  
        # Store only the _id of each Fortress instance in items.  
        fortress_ids = [fortress._id for fortress in self.fortresses]  
        return {  
            "_id": self._id,  
            "name": self.name,  
            "fortresses": fortress_ids  
        }  