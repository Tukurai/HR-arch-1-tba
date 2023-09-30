# classes.py

class GameState:
    def __init__(
        self, player_name=None
    ):
        self.player = Player(name=player_name)
        self.map = self.get_map()

        self.items = {
            0: Consumable(id=0, name="Bottle of water", description="A wet looking drink", restore_amount=1),
            1: Item(id=1, name="Cargo hold key", description="It has a tag that says Cargo hold"),
        }

        self.puzzles = {}
        
        self.interactables = {}

    def get_map(self):
        game_map = Map(5, 5)

        # Bridge 0, 0
        room_items = [
            self.items[0]
        ]
        puzzle_items = [
            self.items[1]
        ]
        puzzles = [
            Puzzle(
                id=0,
                name="Bridge front desk lock",
                unlock_item=puzzle_items
            )
        ]
        interactables = [
            Interactable(
                id=0,
                name="Bridge front desk",
                description="A large desk",
                is_locked=True,
            )
        ]
        room = Room(
                id=0, 
                name="Bridge", 
                description="The control center of the spaceship.",
                is_locked=False,
                interactables=interactables,
                puzzles=puzzles,
                items=room_items
            )
        game_map.add_room(room, 0, 0)


        # ETC ETC

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


class Player:
    def __init__(
        self, name=None, hitpoints=10, inventory=[], weapons=[], current_room=None
    ):
        self.name = name
        self.hitpoints = hitpoints
        self.inventory = inventory
        self.weapons = weapons
        self.current_room = current_room

    def inventory_add(self, items):
        self.inventory += items


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
        was_looked_around=False
    ):
        self.id = id
        self.name = name
        self.description = description
        self.is_locked = is_locked
        self.interactables = interactables
        self.puzzles = puzzles
        self.items = items
        self.enemies = enemies
        self.was_looked_around = was_looked_around


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
