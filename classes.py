
import json
import os


class GamesaveState:
    @classmethod
    def loadstate(cls, save_dict):
        gameobjects = {
            "Player": Player(**save_dict["Player"]),
            "Enemy": [Enemy(**e) for e in save_dict["Enemy"]],
            "Item": [Item(**i) for i in save_dict["Item"]],
            "Weapon": [Weapon(**w) for w in save_dict["Weapon"]],
            "Consumable": [Consumable(**c) for c in save_dict["Consumable"]],
            "Interactable": [Interactable(**i) for i in save_dict["Interactable"]],

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
            "Enemy": GameobjectData.get_enemy_list(),
            "Item": GameobjectData.get_item_list(),
            "Weapon": GameobjectData.get_weapon_list(),
            "Consumable": GameobjectData.get_consumable_list(),
            "Interactable": GameobjectData.get_interactable_list()
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
            Enemy(id=0, name="Spacerat", description="It's a rat, but in space!", hitpoints=1, item_drops=None)
        ]
        return enemy_list
    
    @classmethod
    def get_interactable_list(cls):
        interactable_list = [
            Interactable(id=0, name="desk", description="For working")
        ]
        return interactable_list


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


class Enemy:
    def __init__(self, id=None, name=None, description=None, hitpoints=1, item_drops=None):
        self.id = id
        self.name = name
        self.description = description
        self.hitpoints = hitpoints
        self.item_drops = item_drops


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
    def __init__(self, id=None, name=None, description=None, interactables=None, items=None, enemies=None):
        if interactables is None:
            interactables = []
        if items is None:
            items = []
        if enemies is None:
            items = []

        self.id = id
        self.name = name
        self.description = description
        self.interactables = interactables
        self.items = items
        self.enemies = enemies


class Interactable:
    def __init__(self, id=None, name=None, description=None, items=None, enemies=None):
        if items is None:
            items = []
        if enemies is None:
            enemies = []

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