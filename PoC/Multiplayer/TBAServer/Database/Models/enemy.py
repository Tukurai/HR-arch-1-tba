class Enemy:
    def __init__(self, id, name):
        self._id = id
        self.name = name

    # This method converts the Enemy instance to a dictionary.
    def to_dict(self):
        data = {"name": self.name}

        if self._id is not None:
            data["_id"] = self._id

        return data
