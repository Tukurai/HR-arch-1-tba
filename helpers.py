# helpers.py

class MapHelper:
    @staticmethod
    def get_room_by_id(room_id, rooms):
        for row in rooms:
            for room in row:
                if room is not None and room.id == room_id:
                    return room

    @staticmethod
    def get_room_to_north_of(room, rooms):
        for y in range(len(rooms)):
            for x in range(len(rooms[y])):
                if rooms[y][x] == room and y > 0:
                    return rooms[y - 1][x]
        return None

    @staticmethod
    def get_room_to_south_of(room, rooms):
        for y in range(len(rooms)):
            for x in range(len(rooms[y])):
                if rooms[y][x] == room and y < len(rooms) - 1:
                    return rooms[y + 1][x]
        return None

    @staticmethod
    def get_room_to_west_of(room, rooms):
        for y in range(len(rooms)):
            for x in range(len(rooms[y])):
                if rooms[y][x] == room and x > 0:
                    return rooms[y][x - 1]
        return None

    @staticmethod
    def get_room_to_east_of(room, rooms):
        for y in range(len(rooms)):
            for x in range(len(rooms[y])):
                if rooms[y][x] == room and x < len(rooms[y]) - 1:
                    return rooms[y][x + 1]
        return None


class PlayerHelper:
    @staticmethod
    def add_items_to_inventory(player, item_list):
        for item in item_list:
            player.inventory.append(item)
        
    
    @staticmethod
    def remove_items_from_inventory(player, item_list):
        for item in item_list:
            player.inventory.remove(item)


class GameobjectHelper:
    @staticmethod
    def get_gameobject_by_id(list, id):
        for i in list:
            if i.id == id:
                return i
        return None
