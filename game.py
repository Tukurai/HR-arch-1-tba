import json
import os


def main():
    if start_game() == False:
        gameobjects = Init.initstate()
    
    if input("Would you like to save the game? (y/n): ") == "y":
        player = gameobjects["player"]
        Save.savestate(gameobjects, gameobjects["player"])


def start_game():
    try:
        print("Trying to create saves folder...")
        os.mkdir("saves")
    except FileExistsError:
        print("/saves/ folder found: ")
        pass

    if input("Would you like to load a previous game or start a new one? (load/new): ") == "load":
        savefile_list = []
        for root, dirs, files in os.walk("saves"):
            for file in files:
                if file.endswith(".json"):
                    print(f"{file}")
                    savefile_list.append(file)
        
        if len(savefile_list) != 0:
            while True:
                user_load = input("Which save file would you like to load? (please enter file name with .json extension): ")
                if user_load in savefile_list:
                    with open(user_load, "r") as file:
                        # This does not work yet. Load.loadstate() should take a dict as input.
                        Load.loadstate(file)
                    return True
                else:
                    print("File not found. Please enter a valid file name.")
        else:
            print("No save files found.")
    return False

class Init:
    @classmethod
    def initstate(cls):
        gameobjects = {}
        player_name = input("Please enter your name: ")

        gameobjects["player"] = Player(name=player_name)

        return gameobjects


class Load:
    @classmethod
    def loadstate(cls, savefile):
        gameobjects = {}

        gameobjects["player"] = Player(save=savefile)


class Save:
    @classmethod
    def savestate(cls, gameobjects, player):
        player = gameobjects["player"]
        try:
            file_name = f"{player.name}-save.json"
            
            with open(file_name, "r") as file:
                if len(file.readlines()) != 0:
                    answer = input("There's already a save file present, would you like to overwrite the previous save? (y/n): ")
                    if answer == "n":
                        print("Game not saved")
                        return
        except FileNotFoundError:
            print("No save file found, creating new file")

        os.chdir("saves")
        with open(file_name, "w") as file:
            print("Saving game...")
        
            for gameobject in gameobjects:
                json.dump(gameobjects[gameobject].to_dict(), file)
            print("Game saved succesfully")


class Item():
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Player:
    def __init__(self, name=None, hitpoints=10, inventory=[], weapons=[], save=None):
        if save is not None:
            self.__dict__ = save
        else:
            self.name = name
            self.hitpoints = hitpoints
            self.inventory = inventory
            self.weapons = weapons
    
    def to_dict(self):
        data = {"name": self.name, "hitpoints": self.hitpoints, "inventory": self.inventory, "weapons": self.weapons}
        return data


class Room():
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Weapon():
    def __init__(self, id, name, damage):
        self.id = id
        self.name = name
        self.damage = damage


if __name__ == "__main__":
    main()