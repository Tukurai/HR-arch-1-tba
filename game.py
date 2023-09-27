import json
import os


def main():
    object_dict = start_game()

    if object_dict is not None:
        gameobjects = GamesaveState.loadstate(object_dict)
    else:
        gameobjects = GameobjectData.init_gameobject_data()

    # Saves the game in its current state
    if input("Would you like to save the game? (y/n): ") == "y":
        GamesaveState.savestate(gameobjects)


def start_game():
    try:
        print("Trying to create saves folder...")
        os.mkdir("saves")
    except FileExistsError:
        print("/saves/ folder found: ")
        pass

    if (
        input("Would you like to load a previous game or start a new one? (load/new): ")
        == "load"
    ):
        savefile_list = []
        for root, dirs, files in os.walk("saves"):
            for file in files:
                if file.endswith(".json"):
                    print(f"{file}")
                    savefile_list.append(file)

        if len(savefile_list) != 0:
            while True:
                user_load = input(
                    "Which save file would you like to load? (please enter file name with .json extension): "
                )
                if user_load in savefile_list:
                    if not os.getcwd().endswith("saves"):
                        os.chdir("saves")

                    with open(user_load, "r") as json_file:
                        return json.load(json_file)
                else:
                    print("File not found. Please enter a valid file name.")
        else:
            print("No save files found.")
    return None


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
    def __init__(self, name=None, hitpoints=10, inventory=None, weapons=None):
        if inventory is None:
            inventory = []
        if weapons is None:
            weapons = []

        self.name = name
        self.hitpoints = hitpoints
        self.inventory = inventory
        self.weapons = weapons

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
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name


if __name__ == "__main__":
    main()