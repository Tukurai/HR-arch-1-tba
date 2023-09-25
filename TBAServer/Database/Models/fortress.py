class Fortress:
    def __init__(self, id, name, floors=None):
        self._id = id
        self.name = name
        self.floors = floors if floors is not None else []

    def add_floor(self, floor):
        if self._id is not None:
            self.floors.append(floor)

    # This method converts the Fortress instance to a dictionary.
    def to_dict(self):
        # Store only the _id of each Floor instance in floors.
        floor_ids = [floor._id for floor in self.floors]

        data = {"name": self.name, "floors": floor_ids}

        if self._id is not None:
            data["_id"] = self._id

        return data