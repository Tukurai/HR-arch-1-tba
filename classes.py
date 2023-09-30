# classes.py

class GameState:
    def __init__(
        self, player_name=None
    ):
        self.player = Player(name=player_name)

        self.enemies = {  
            0: Enemy(id=0, name="Spacerat", description="A rat!... in space!", hitpoints=2, level=1, damage=1, aggressive=False),  
            1: Enemy(id=1, name="Alien Trooper", description="A hostile extraterrestrial soldier with advanced weaponry.", hitpoints=5, level=2, damage=2, aggressive=True),  
            2: Enemy(id=2, name="Energy parasite", description="A biomechanical creature that feeds on the facility's power systems", hitpoints=4, level=2, damage=1, aggressive=True),  
            3: Enemy(id=3, name="Nightmare shadow", description="Mysterious shadowy entity that haunts dreams, causing sleep deprivation and hallucinations.", hitpoints=4, level=3, damage=2, aggressive=True),  
            4: Enemy(id=4, name="Galactic Pirate", description="A space outlaw known for their ruthlessness.", hitpoints=6, level=3, damage=2, aggressive=True),  
            5: Enemy(id=5, name="Galactic Pirate Captain", description="Leader of the space outlaws, known for their exceptional strength and cruelty.", hitpoints=8, level=4, damage=3, aggressive=True),  
            6: Enemy(id=6, name="Alien Queen", description="The ruler of the alien horde. Extremely dangerous.", hitpoints=10, level=5, damage=4, aggressive=True),
            7: Enemy(id=7, name="Void Walker", description="A creature from the void of space, invisible until it's too late.", hitpoints=7, level=4, damage=3, aggressive=True),  
            8: Enemy(id=8, name="Star Serpent", description="A massive serpent-like creature that travels the stars.", hitpoints=10, level=5, damage=4, aggressive=True),  
            9: Enemy(id=9, name="Meteor Golem", description="A golem made from hardened meteorite, incredibly durable.", hitpoints=12, level=6, damage=3, aggressive=True),  
            10: Enemy(id=10, name="Cosmic Horror", description="A terrifying entity from the edges of reality.", hitpoints=14, level=7, damage=4, aggressive=True),  
        }  
  
        self.items = {  
            0: Consumable(id=0, name="Bottle of water", description="A wet looking drink", restore_amount=1),  
            1: Item(id=1, name="Cargo hold key", description="It has a tag that says Cargo hold"),  
            2: Weapon(id=2, name="Laser Pistol", description="Standard issue sidearm for most space forces. It can cause a decent amount of damage.", damage_multiplier=3),  
            3: Item(id=3, name="Engine part", description="A part for a spaceship engine. It looks usable"),  
            4: Consumable(id=4, name="Alien fruit", description="A strange looking fruit. Eating it might restore some health.", restore_amount=2),  
            5: Weapon(id=5, name="Plasma Sword", description="A weapon made of pure energy. It can cause a lot of damage.", damage_multiplier=5),  
            6: Item(id=6, name="Alien artifact", description="An ancient alien artifact. Its use is unknown."),  
            7: Consumable(id=7, name="Energy drink", description="A drink that boosts your energy. It will restore your health.", restore_amount=3),  
            8: Item(id=8, name="Space suit", description="A suit that allows you to survive in the harsh conditions of space."),  
            9: Weapon(id=9, name="Rocket Launcher", description="A powerful weapon that can cause a huge amount of damage.", damage_multiplier=7),
            10: Consumable(id=10, name="Health pack", description="A medical pack that restores alot of health", restore_amount=10),
            11: Item(id=11, name="Front desk key", description="A key that happens to look like it could fit a desk lock"),  
            12: Item(id=12, name="Cargo hold key", description="An old but futuristic key"),  
            13: Item(id=13, name="Armory access code", description="A digital card that says: 8340"),  
            14: Item(id=14, name="Star map", description="There are coordinates on the map: 36-24-36"),
            15: Item(id=15, name="Ancient key", description="A mysterious old key. It looks like it could unlock something important."),
            16: Item(id=16, name="Alien encryption device", description="The device just prints out the number 42..."),
            17: Item(id=17, name="Storage room key", description="A key that unlocks the storage room"),
            18: Item(id=18, name="Science lab access code", description="A digital card that says: 9493")
        }
  
        self.puzzles = {  
            0: Puzzle(id=0, name="Bridge front desk lock", unlock_item=self.items[11]),  
            1: Puzzle(id=1, name="Cargo hold door lock", unlock_item=self.items[12]),  
            2: Puzzle(id=2, name="Armory keypad", question="Enter the passcode", solution="8340"),  
            3: Puzzle(id=3, name="Galactic coordinates", question="What are the coordinates to the nearest safe planet?", solution="36-24-36", unlock_item=self.items[14]),
            4: Puzzle(id=4, name="Ancient chest lock", unlock_item=self.items[15]),
            5: Puzzle(id=5, name="Alien encryption", question="Can you decipher the alien language?", solution="42"),
            6: Puzzle(id=6, name="Storage room lock", unlock_item=self.items[17]),
            7: Puzzle(id=7, name="Science lab keypad", question="Enter the passcode", solution="9493")
        }  
          
        self.interactables = {  
            0: Interactable(id=0, name="Bridge front desk", description="A large desk", is_locked=True, items=[self.items[1]], puzzles=[self.puzzles[0]]),  
            1: Interactable(id=1, name="Alien plant", description="A strange looking plant. Maybe it has some useful items?", items=[self.items[4]]),  
            2: Interactable(id=2, name="Old spaceship", description="A derelict spaceship. Perhaps there are useful items inside.", items=[self.items[2]], enemies=[self.enemies[1]]),  
            3: Interactable(id=3, name="Ancient chest", description="An ancient alien chest.", items=[self.items[6]], puzzles=[self.puzzles[4]]),  
            4: Interactable(id=4, name="Space suit locker", description="A locker containing space suits.", items=[self.items[8]])  
        }  

        self.map = self.get_map()

    def get_map(self):
        game_map = Map(5, 5)

        # Bridge 0, 0
        game_map.add_room(
            Room(
                id=0, 
                name="Bridge", 
                description="The control center of the spaceship.",
                is_locked=False,
                interactables=[self.interactables.get(key) for key in [0]],
                puzzles=[self.puzzles.get(key) for key in [0]],
            ),
            0,
            0,
        )

        # Engine room 1, 0
        game_map.add_room(
            Room(
                id=1,
                name="Engine Room",
                description="A room filled with loud machinery.",
                is_locked=False,
                items=[self.items.get(key) for key in [2, 3]],
                enemies=[self.enemies.get(key) for key in [2]]
            ),
            1,
            0,
        )

        # Cargo hold 2, 0
        game_map.add_room(
            Room(
                id=2, 
                name="Cargo Hold", 
                description="A large room for storing cargo.",
                is_locked=True,
                items=[self.items.get(key) for key in [6]],
                puzzles=[self.puzzles.get(key) for key in [1]],
            ),
            2,
            0,
        )

        # Crew quarters 3, 0
        game_map.add_room(
            Room(
                id=3, 
                name="Crew Quarters", 
                description="Where the crew sleeps.",
                is_locked=False,
                items=[self.items.get(key) for key in [7, 8]],
                enemies=[self.enemies.get(key) for key in [4]]
            ), 
            3, 
            0,
        )

        # Medical bay 4, 0
        game_map.add_room(
            Room(
                id=4,
                name="Medical Bay",
                description="A clean room with medical equipment.",
                is_locked=False,
                items=[self.items.get(key) for key in [10, 18]],
            ),
            4,
            0,
        )

        # Kitchen 0, 1
        game_map.add_room(
            Room(
                id=5, 
                name="Kitchen", 
                description="A room with cooking equipment.",
                is_locked=False,
                items=[self.items.get(key) for key in [4]],
                enemies=[self.enemies.get(key) for key in [0]]
            ),
            0,
            1,
        )

        # Dining room 1, 1
        game_map.add_room(
            Room(
                id=6,
                name="Dining Room",
                description="A room with tables and chairs for eating.",
                is_locked=False
            ),
            1,
            1,
        )

        # Bathroom 2, 1
        game_map.add_room(
            Room(
                id=7,
                name="Bathroom",
                description="A small room with a shower and toilet.",
                is_locked=False,
                items=[self.items.get(key) for key in [17]],
            ),
            2,
            1,
        )

        # Storage room 3, 1
        game_map.add_room(
            Room(
                id=8,
                name="Storage Room",
                description="A room filled with various supplies.",
                is_locked=True,
                items=[self.items.get(key) for key in [2]],
                puzzles=[self.puzzles.get(key) for key in [6]]
            ),
            3,
            1,
        )

        # Airlock 4, 1
        game_map.add_room(
            Room(
                id=9,
                name="Airlock",
                description="A room used for exiting and entering the spaceship.",
                is_locked=True,
                puzzles=[self.puzzles.get(key) for key in [5]],
                enemies=[self.enemies.get(key) for key in [10]]
            ),
            4,
            1,
        )

        # Observation Desk 0, 2
        game_map.add_room(
            Room(
                id=10,
                name="Observation Deck",
                description="A room with large windows for viewing space.",
                is_locked=False,
                items=[self.items.get(key) for key in [11]],
                enemies=[self.enemies.get(key) for key in [0]]
            ),
            0,
            2,
        )

        game_map.add_room(
            Room(
                id=11, 
                name="Gym", 
                description="A room with exercise equipment.",
                is_locked=False,
                interactables=[self.interactables.get(key) for key in [1]],
            ), 
            1, 
            2
        )

        # Science lab 2, 2
        game_map.add_room(
            Room(
                id=12,
                name="Science Lab",
                description="A room filled with scientific equipment.",
                is_locked=True,
                items=[self.items.get(key) for key in [16, 10, 5]],
                puzzles=[self.puzzles.get(key) for key in [7]],
                enemies=[self.enemies.get(key) for key in [5]]
            ),
            2,
            2,
        )

        # Escape pod bay 3, 2
        game_map.add_room(
            Room(
                id=13,
                name="Escape Pod Bay",
                description="A room housing escape pods for emergencies.",
                is_locked=False,
                interactables=[self.interactables.get(key) for key in [1]],
            ),
            3,
            2,
        )

        # Armory 4, 2
        game_map.add_room(
            Room(id=14, 
                name="Armory", 
                description="A room storing weapons and armor.",
                is_locked=True,
                items=[self.items.get(key) for key in [9]],
                puzzles=[self.puzzles.get(key) for key in [7]],
                interactables=[self.interactables.get(key) for key in [4]],
            ),
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
