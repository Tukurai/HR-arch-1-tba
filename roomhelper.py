class RoomHelper:  
    @staticmethod  
    def get_room_by_id(room_id, rooms):  
        for row in rooms:  
            for room in row:  
                if room is not None and room.id == room_id:  
                    return room  
  
    @staticmethod  
    def get_adjacent_rooms(current_room, rooms):  
        # This will depend on how you structure your rooms, but it could be something like this  
        adjacent_rooms = []  
        for row in rooms:  
            for room in row:  
                if room is not None:  
                    if room.x == current_room.x and abs(room.y - current_room.y) == 1:  
                        adjacent_rooms.append(room)  
                    elif room.y == current_room.y and abs(room.x - current_room.x) == 1:  
                        adjacent_rooms.append(room)  
        return adjacent_rooms  
