# classes.py

class GameState:
    @classmethod
    def init_game_state(cls, player_name):
        game_state = {
            "Player": Player(name=player_name),
            "Enemy": GameState.get_enemy_list(),
            "Item": GameState.get_item_list(),
            "Weapon": GameState.get_weapon_list(),
            "Consumable": GameState.get_consumable_list(),
            "Interactable": GameState.get_interactable_list(),
            "Puzzle": GameState.get_puzzle_list(),
            "Map": GameState.get_map(),
        }

        return game_state

    @classmethod
    def get_item_list(cls):
        item_list = [
            Item(id=0, name="Bridge desk key", description="A futuristic but old looking key"),
            Item(id=1, name="Armory code note", description="There's a code scribbled on the note: 5598")
            ]
        return item_list

    @classmethod
    def get_consumable_list(cls):
        consumable_list = [
            Consumable(id=0, name="Piece of bread", description="It looks a little dry +1hp", restore_amount=1),
            Consumable(id=1, name="Bottle of water", description="Fresh bottled water +1hp", restore_amount=1),
            Consumable(id=2, name="Bandage", description="To wrap around wounds +3hp", restore_amount=3),
            Consumable(id=3, name="Health pack", description="A proper health pack +10hp", restore_amount=10)
        ]
        return consumable_list

    @classmethod
    def get_weapon_list(cls):
        weapon_list = [
            Weapon(id=0, name="Spaceknife", description="A futuristic looking knife", damage_multiplier=1),
            Weapon(id=1, name="Mining laser", description="A laser meant for mining, but it looks like it could do some damage to other things", damage_multiplier=1.2),
            Weapon(id=2, name="Lightsaber", description="Somehow, it looks familiar", damage_multiplier=1.5)
            ]
        return weapon_list

    @classmethod
    def get_enemy_list(cls):
        enemy_list = [
            Enemy(
                id=0,
                name="Spacerat",
                description="It's a rat, but in space!",
                hitpoints=2,
                level=1,
                damage=1,
                item_drops=None,
                aggressive=False
            ),
            Enemy(
                id=1,
                name="Spaceworm",
                description="Eek!!!",
                hitpoints=2,
                level=1,
                damage=1,
                item_drops=None,
                aggressive=True
            )
        ]
        return enemy_list

    @classmethod
    def get_interactable_list(cls):
        interactable_list = [Interactable(id=0, name="desk", description="For working")]
        return interactable_list

    @classmethod
    def get_map(cls):
        game_map = Map(5, 5)
        game_map.add_room(
            Room(
                id=0, name="Bridge", description="The control center of the spaceship."
            ),
            0,
            0,
        )
        game_map.add_room(
            Room(
                id=1,
                name="Engine Room",
                description="A room filled with loud machinery.",
            ),
            1,
            0,
        )
        game_map.add_room(
            Room(
                id=2, name="Cargo Hold", description="A large room for storing cargo."
            ),
            2,
            0,
        )
        game_map.add_room(
            Room(id=3, name="Crew Quarters", description="Where the crew sleeps."), 3, 0
        )
        game_map.add_room(
            Room(
                id=4,
                name="Medical Bay",
                description="A clean room with medical equipment.",
            ),
            4,
            0,
        )
        game_map.add_room(
            Room(id=5, name="Kitchen", description="A room with cooking equipment."),
            0,
            1,
        )
        game_map.add_room(
            Room(
                id=6,
                name="Dining Room",
                description="A room with tables and chairs for eating.",
            ),
            1,
            1,
        )
        game_map.add_room(
            Room(
                id=7,
                name="Bathroom",
                description="A small room with a shower and toilet.",
            ),
            2,
            1,
        )
        game_map.add_room(
            Room(
                id=8,
                name="Storage Room",
                description="A room filled with various supplies.",
            ),
            3,
            1,
        )
        game_map.add_room(
            Room(
                id=9,
                name="Airlock",
                description="A room used for exiting and entering the spaceship.",
            ),
            4,
            1,
        )
        game_map.add_room(
            Room(
                id=10,
                name="Observation Deck",
                description="A room with large windows for viewing space.",
            ),
            0,
            2,
        )
        game_map.add_room(
            Room(id=11, name="Gym", description="A room with exercise equipment."), 1, 2
        )
        game_map.add_room(
            Room(
                id=12,
                name="Science Lab",
                description="A room filled with scientific equipment.",
            ),
            2,
            2,
        )
        game_map.add_room(
            Room(
                id=13,
                name="Escape Pod Bay",
                description="A room housing escape pods for emergencies.",
            ),
            3,
            2,
        )
        game_map.add_room(
            Room(id=14, name="Armory", description="A room storing weapons and armor."),
            4,
            2,
        )
        return game_map

    @classmethod
    def get_puzzle_list(cls):
        puzzle_list = [
            Puzzle(id=0, name="Armory keypad", question="Please enter the 4-number access key", solution="5598", unlock_item=None),
            Puzzle(id=1, name="Bridge desk lock", question="This could fit a key", solution=None, unlock_item=...)
        ]
        return puzzle_list


class Player:
    def __init__(
        self, name=None, hitpoints=10, inventory=[], weapons=[], current_room=None
    ):
        self.name = name
        self.hitpoints = hitpoints
        self.inventory = inventory
        self.weapons = weapons
        self.current_room = current_room

    def inventory_add(self, item):
        self.inventory.append(item)


class Enemy:
    def __init__(
        self,
        id=None,
        name=None,
        description=None,
        hitpoints=1,
        level=None,
        damage=None,
        item_drops=None,
        aggressive=None,
    ):
        if item_drops is None:
            item_drops = []

        self.id = id
        self.name = name
        self.description = description
        self.level = level
        self.damage = damage
        self.hitpoints = hitpoints
        self.item_drops = item_drops
        self.aggresive = aggressive


class Item:
    def __init__(self, id=None, name=None, description=None):
        self.id = id
        self.name = name
        self.description = description


class Weapon(Item):
    def __init__(self, id=None, name=None, description=None, damage_multiplier=1):
        super().__init__(id, name, description)
        self.damage_multiplier = damage_multiplier


class Consumable(Item):
    def __init__(self, id=None, name=None, description=None, restore_amount=1):
        super().__init__(id, name, description)
        self.restore_amount = restore_amount


class Room:
    def __init__(
        self,
        id=None,
        name=None,
        description=None,
        is_locked=None,
        interactables=[],
        puzzles=[],
        items=[],
        enemies=[],
    ):
        self.id = id
        self.name = name
        self.description = description
        self.is_locked = is_locked
        self.interactables = interactables
        self.puzzles = puzzles
        self.items = items
        self.enemies = enemies


class Interactable:
    def __init__(self, id=None, name=None, description=None, is_locked=None, items=[], enemies=[], puzzles=[]):
        self.id = id
        self.name = name
        self.description = description
        self.is_locked = is_locked
        self.items = items
        self.enemies = enemies
        self.puzzles = puzzles


class Puzzle:
    def __init__(self, id=None, name=None, question=None, solution=None, unlock_item=None):
        self.id = id
        self.name = name
        self.question = question
        self.solution = solution
        self.unlock_item = unlock_item


class Map:
    def __init__(self, width, height):
        self.rooms = [[None for _ in range(width)] for _ in range(height)]

    def add_room(self, room, x, y):
        self.rooms[y][x] = room
