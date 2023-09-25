class Floor:
    def __init__(self, id, name, rooms=None):
        self._id = id
        self.name = name
        self.rooms = rooms if rooms is not None else []

    def add_room(self, room):
        if self._id is not None:
            self.rooms.append(room)

    # This method converts the Floor instance to a dictionary.
    def to_dict(self):
        # Store only the _id of each Room instance in rooms.
        room_ids = [room._id for room in self.rooms]

        data = {"name": self.name, "rooms": room_ids}

        if self._id is not None:
            data["_id"] = self._id

        return data
