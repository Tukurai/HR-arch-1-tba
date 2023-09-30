# classes.py

import json
import os


class GamesaveState:
    @classmethod
    def loadstate(cls, save_dict):
        gameobjects = {
            "Player": Player(**save_dict["Player"]),
            "Map": Map(**save_dict["Map"]),
        }

        # for row in save_dict["Map"]["rooms"]:
        #     for room in row ???????????????????????

        return gameobjects

    @classmethod
    def savestate(cls, gameobjects):
        file_name = f"{gameobjects['Player'].name}-save.json"

        if not os.getcwd().endswith("saves"):
            os.chdir("saves")

        with open(file_name, "w") as file:
            print("Saving game...")
            json.dump(gameobjects, file, default=lambda o: o.__dict__)
            print("Game saved successfully")


class GameobjectData:
    @classmethod
    def init_gameobject_data(cls):
        player_name = input("Please enter your name: ")

        gameobjects = {
            "Player": Player(name=player_name),
            "Enemy": GameobjectData.get_enemy_list(),
            "Item": GameobjectData.get_item_list(),
            "Weapon": GameobjectData.get_weapon_list(),
            "Consumable": GameobjectData.get_consumable_list(),
            "Interactable": GameobjectData.get_interactable_list(),
            "Map": GameobjectData.get_map(),
        }

        return gameobjects

    @classmethod
    def get_item_list(cls):
        item_list = [Item(id=0, name="Spaceship key")]
        return item_list

    @classmethod
    def get_consumable_list(cls):
        consumable_list = [
            Consumable(id=0, name="Piece of bread", restore_amount=1),
            Consumable(id=1, name="Bottle of water", restore_amount=1),
        ]
        return consumable_list

    @classmethod
    def get_weapon_list(cls):
        weapon_list = [Weapon(id=0, name="Spaceknife", damage_multiplier=1)]
        return weapon_list

    @classmethod
    def get_enemy_list(cls):
        enemy_list = [
            Enemy(
                id=0,
                name="Spacerat",
                description="It's a rat, but in space!",
                hitpoints=1,
                item_drops=None,
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
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name


class Weapon(Item):
    def __init__(self, id=None, name=None, damage_multiplier=1):
        super().__init__(id, name)
        self.damage_multiplier = damage_multiplier


class Consumable(Item):
    def __init__(self, id=None, name=None, restore_amount=1):
        super().__init__(id, name)
        self.restore_amount = restore_amount


class Room:
    def __init__(
        self,
        id=None,
        name=None,
        description=None,
        interactables=[],
        items=[],
        enemies=[],
    ):
        self.id = id
        self.name = name
        self.description = description
        self.interactables = interactables
        self.items = items
        self.enemies = enemies


class Interactable:
    def __init__(self, id=None, name=None, description=None, items=[], enemies=[]):
        self.id = id
        self.name = name
        self.description = description
        self.items = items
        self.enemies = enemies


class Map:
    def __init__(self, width, height):
        self.rooms = [[None for _ in range(width)] for _ in range(height)]

    def add_room(self, room, x, y):
        self.rooms[y][x] = room
