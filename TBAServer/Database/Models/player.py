class Player:
    def __init__(self, id, name, password):
        self._id = id
        self.name = name
        self.password = password

    def to_dict(self):
        data = {"name": self.name, "password": self.password}

        if self._id is not None:
            data["_id"] = self._id

        return data

    # This static method creates a new Player instance from a dictionary.
    @staticmethod
    def from_dict(data):
        return Player(data["_id"], data["name"], data["password"])
