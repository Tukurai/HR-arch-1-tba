class Enemy:  
    def __init__(self, _id, name):
        self._id = _id
        self.name = name

    # This method converts the Enemy instance to a dictionary.  
    def to_dict(self):  
        return {  
            "_id": self._id,  
            "name": self.name
        }  