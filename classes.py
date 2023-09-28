
import json
import os


class GamesaveState:
    @classmethod
    def loadstate(cls, save_dict):
        gameobjects = {
            "Player": Player(**save_dict["Player"]),
            "Item": [Item(**i) for i in save_dict["Item"]],
            "Consumable": [Consumable(**c) for c in save_dict["Consumable"]],
            "Weapon": [Weapon(**w) for w in save_dict["Weapon"]],
        }
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
            "Item": GameobjectData.get_item_list(),
            "Consumable": GameobjectData.get_consumable_list(),
            "Weapon": GameobjectData.get_weapon_list(),
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


class Player:
    def __init__(self, name=None, hitpoints=10, inventory=None, weapons=None, current_room=None):
        if inventory is None:
            inventory = []
        if weapons is None:
            weapons = []

        self.name = name
        self.hitpoints = hitpoints
        self.inventory = inventory
        self.weapons = weapons
        self.current_room = current_room

    def inventory_add(self, item):
        self.inventory.append(item)


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
    def __init__(self, id=None, name=None, description=None):
        self.id = id
        self.name = name
        self.description = description
        
class Map:
    def __init__(self, width, height):
        self.rooms = [[None for _ in range(width)] for _ in range(height)]

    def add_room(self, room, x, y):
        self.rooms[y][x] = room
