def main():
    # Init directions
    north = Direction("NORTH", "FORWARD")
    east = Direction("EAST", "RIGHT")
    south = Direction("SOUTH", "BACKWARD")
    west = Direction("WEST", "LEFT")
    directions = [north, east, south, west]

    # Init items
    items = []
    items.append(Item(0, "Cargobay Key", "Key"))
    items.append(Item(1, "Spacelaser", "Weapon"))

    # Init rooms
    start = Room(0, "Start", None, None, None, None, None, False, None)
    spaceship_entry = Room(1, "Spaceship Entry", None, None, None, None, None, False, None)
    spaceship_hallway = Room(2, "Spaceship Hallway", None, None, None, None, None, False, None)
    spaceship_cargobay = Room(3, "Spaceship Cargobay", None, None, None, None, [items[1]], True, items[0])
    spaceship_cockpit = Room(4, "Spaceship Cockpit", None, None, None, None, [items[0]], False, None)

    start.add_description("The floor is made of some kind of sand and you are surrounded by rocks. It doesn't look familiar to you. You see a spaceship ahead")
    spaceship_entry.add_description("The door creaks as it opens. You walk inside the damaged spaceship")
    spaceship_hallway.add_description("You seem to have entered some hallway. The air is thick with the smell of fuel.")
    spaceship_cargobay.add_description("There seems to be a bunch cargo here. Maybe there's something handy or valueable to be found")
    spaceship_cockpit.add_description("The cockpit is completely destroyed. It must have been some crash!. You see a key on the floor beneath cockpit chair.")

    start.path_north = spaceship_entry

    spaceship_entry.path_north = spaceship_hallway
    spaceship_entry.path_south = start

    spaceship_hallway.path_east = spaceship_cargobay
    spaceship_hallway.path_west = spaceship_cockpit
    spaceship_hallway.path_south = spaceship_entry

    spaceship_cargobay.path_west = spaceship_hallway
    
    spaceship_cockpit.path_east = spaceship_hallway

    # Start game
    inp = input("Please enter your name: ")
    player = Player(inp, start, [])
    print(f"Hello {player.name}, you are stranded on an alien planet with no memory of how you got here.")

    # Game loop
    while True:
        inp = ask_input()
        process_input(player, inp, items, directions)
        if inp == "exit":
            print("Thank you for playing!")
            break
            

def ask_input():
    return input("What do you want to do?: ")


def process_input(player, inp, items, directions):
    # Possible commands that correspond to actions
    move_words = ["MOVE", "GO", "WALK"]
    pick_up_words = ["PICK UP", "GRAB", "TAKE"]
    look_around_words = ["LOOK AROUND", "CHECK"]
    use_words = ["USE"]

    # Move player
    for word in move_words:
        if word in inp.upper():

            # Check for which direction to move in
            for direction in directions:
                for direction_comp in direction.get_list():
                    if direction_comp in inp.upper():

                        # Pass player and direction to move function, returns -1, 0 or 1
                        move_return = move(player, direction)
                        match move_return:
                            case -1:
                                print("The room appears to be locked")
                                return
                            case 0:
                                print("There's no path there")
                            case 1:
                                text = direction.nesw.lower()
                                print(f"You walk {text.capitalize()}")

    # Pick up item
    for word in pick_up_words:
        if word in inp.upper():

            #Check which item to try to pick up
            for item in items:
                if item.name.upper() in inp.upper() or item.alias.upper() in inp.upper():
                    pick_up_return = pick_up(player, item)
                    if pick_up_return == 1:
                        print(f"You picked up {item.name}")
                        return
                    else:
                        print("You could not find that item here")

    # Look around a room
    for word in look_around_words:
        if word in inp.upper():
            print(look_around(player.room))

    # Use an item
    for word in use_words:
        if word in inp.upper():

            # Check which item to use
            for item in items:
                if item.name.upper() in inp.upper() or item.alias.upper() in inp.upper():
                    use_return = use(player, item)
                    match use_return:
                        case 1:
                            print(f"You succesfully used {item.name}")
                        case 0:
                            print(f"{item.name} can't be used here")
                        case -1:
                            print(f"You don't have {item.name}")        


def move(player, direction):
    """
    Tries to move player in direction. 
    returns -1 if room is locked, 
    0 if path doesnt lead to room, 
    1 if player moved succesfully
    """

    path = player.room.get_path(direction)
    if path == None:
        print("DEBUG: You can't go that way! <path = None> -> return 0")
        return 0
    elif path.is_locked == True:
        print(f"DEBUG: Door to {path} is locked! <path.locked = True -> return -1>")
        return -1
    else:
        player.room = path
        print(f"DEBUG: Moved player to {path} -> return 1")
        return 1


def pick_up(player, item):
    """
    Tries to pick up an item.
    Returns 1 if player succesfully picked up the item
    Returns 0 when item not in the current room
    """
    if item in player.room.items:
        player.inventory.append(item)
        player.room.destroy_item(item)
        print(f"DEBUG: Item destroyed in room, {player.room.items} pick_up() -> return 1")
        print(f"DEBUG: Item found in room, added to player inventory: {player.inventory} pick_up() -> return 1")
        return 1
    else:
        print("Item not found in room pick_up() -> return 0")
        return 0


def look_around(room):
    """
    Simply looks around the room.
    Returns room description from room object
    """
    return room.description


def use(player, item):
    """
    Checks if item is in players inventory.
    Returns 1 if room is unlocked.
    Returns 0 if the key is not the item.
    Returns -1 if item is not in inventory.
    """
    if item in player.inventory:
        print("DEBUG: Item in player inventory! use()")
        for room in player.room.get_paths():
            if room != None:
                print("DEBUG: Room != to None use()")
                if room.key == item:
                    print("DEBUG: Room should unlock use()")
                    room.unlock()
                    return 1
        else:
            return 0    
    else:
        return -1


class Player:
    def __init__(self, name, room, inventory):
        self.name = name
        self.room = room
        self.inventory = inventory
    

    def destroy_item(self, item):
        if item in self.inventory():
            self.inventory.remove(item)

class Room:
    def __init__(self, id, name, path_north, path_east, path_south, path_west, items, is_locked, key):
        self.id = id
        self.name = name
        self.description = ""
        self.path_north = path_north
        self.path_east = path_east
        self.path_south = path_south
        self.path_west = path_west
        self.items = items
        self.is_locked = is_locked
        self.key = key


    def get_paths(self):
        return [self.path_north, self.path_east, self.path_south, self.path_west]


    def add_description(self, description):
        self.description = description


    def destroy_item(self, item):
        "Destroy item in room(ex. when item is picked up)"
        if len(self.items) != 0:
            self.items.remove(item)


    def add_item(self, item):
        "Adds item to the room list"
        self.items.append(item)


    def get_path(self, direction):
        "Converts a direction to a path(room object)"
        match direction.nesw:
            case "NORTH":
                return self.path_north
            case "EAST":
                return self.path_east
            case "SOUTH":
                return self.path_south
            case "WEST":
                return self.path_west
    
    def unlock(self):
        self.is_locked = False


class Item:
    def __init__(self, id, name, alias):
        self.id = id
        self.name = name
        self.alias = alias

class Direction:
    def __init__(self, direction_nesw, direction_frdl):
        "Initialise direction with a NORTH EAST SOUTH WEST part that corresponds with FORWARD RIGHT DOWN LEFT"
        self.nesw = direction_nesw
        self.frdl = direction_frdl
    
    def get_list(self):
        "Return the components as a list"
        return [self.nesw, self.frdl]


if __name__ == "__main__":
    main()