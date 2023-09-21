class Fortress:  
    def __init__(self, _id, name, floors=None):
        self._id = _id
        self.name = name
        self.floors = floors if floors is not None else []  

    def add_floor(self, floor):  
        self.floors.append(floor)  
    
    # This method converts the Fortress instance to a dictionary.  
    def to_dict(self):  
        # Store only the _id of each Floor instance in floors.  
        floor_ids = [floor._id for floor in self.floors]  
        return {  
            "_id": self._id,  
            "name": self.name,  
            "floors": floor_ids  
        }  