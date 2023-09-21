
class Room:  
    def __init__(self, _id, name, items=None):
        self._id = _id
        self.name = name
        self.items = items if items is not None else []  

    def add_item(self, item):  
        self.items.append(item)  
        
    # This method converts the Room instance to a dictionary.  
    def to_dict(self):  
        # Store only the _id of each Item instance in items.  
        item_ids = [item._id for item in self.items]  
        return {  
            "_id": self._id,  
            "name": self.name,  
            "items": item_ids  
        }  