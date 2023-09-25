class Item:
    def __init__(self, _id, name):
        self._id = _id
        self.name = name

    # This method converts the Item instance to a dictionary.
    def to_dict(self):
        data = {"name": self.name}

        if self._id is not None:
            data["_id"] = self._id
        
        return data
