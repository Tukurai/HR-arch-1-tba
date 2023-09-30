# game.py

import os
import random

from handlers import SaveLoadHandler, InputHandler
from helpers import MapHelper, GameobjectHelper, PlayerHelper
from classes import GameobjectData, GamesaveState, Map, Room


def main():
    random.seed()
    object_dict = start_game()
    gameobjects = GameobjectData.init_gameobject_data()

    if object_dict is not None:
        for key, value in GamesaveState.loadstate(object_dict):
            gameobjects[key] = value
    else:
        # Set the player's current room to starting room
        for row in gameobjects["Map"].rooms:
            for room in row:
                if (
                    room is not None and room.id == 0
                ):  # Assuming id=0 is the starting room
                    gameobjects["Player"].current_room = room
                    break

    while True:
        print(
            "You are currently in the {}.".format(
                gameobjects["Player"].current_room.name
            )
        )

        possible_directions = ["north", "south", "west", "east"]
        room_methods = [
            MapHelper.get_room_to_north_of,
            MapHelper.get_room_to_south_of,
            MapHelper.get_room_to_west_of,
            MapHelper.get_room_to_east_of,
        ]
        available_actions = ["investigate", "inventory", "attack", "save", "load", "help"]
        direction_prompts = []

        for direction, method in zip(possible_directions, room_methods):
            new_room = method(
                gameobjects["Player"].current_room, gameobjects["Map"].rooms
            )
            if new_room is not None:
                available_actions.insert(0, f"go {direction}")
                direction_prompts.append(f"go {direction}")

        direction_prompts_string = ", ".join(direction_prompts)
        action_prompt = f"What would you like to do? ({direction_prompts_string}, investigate, inventory, save, load, help): "

        action = InputHandler.user_input(
            action_prompt,
            available_actions,
        )

        print(f"DEBUG action: {action}")
        match action[0]:
            case "go north":
                new_room = MapHelper.get_room_to_north_of(
                    gameobjects["Player"].current_room, gameobjects["Map"].rooms
                )
                if new_room is not None:
                    gameobjects["Player"].current_room = new_room
                else:
                    print("You cannot go north from here.")
            case "go south":
                new_room = MapHelper.get_room_to_south_of(
                    gameobjects["Player"].current_room, gameobjects["Map"].rooms
                )
                if new_room is not None:
                    gameobjects["Player"].current_room = new_room
                else:
                    print("You cannot go south from here.")
            case "go west":
                new_room = MapHelper.get_room_to_west_of(
                    gameobjects["Player"].current_room, gameobjects["Map"].rooms
                )
                if new_room is not None:
                    gameobjects["Player"].current_room = new_room
                else:
                    print("You cannot go west from here.")
            case "go east":
                new_room = MapHelper.get_room_to_east_of(
                    gameobjects["Player"].current_room, gameobjects["Map"].rooms
                )
                if new_room is not None:
                    gameobjects["Player"].current_room = new_room
                else:
                    print("You cannot go east from here.")
            case "investigate":
                current_room = gameobjects["Player"].current_room
                item_list = current_room.items
                interactable_list = current_room.interactables
                enemy_list = []
                if current_room.enemies is not None:
                    for enemy in current_room.enemies:
                        if enemy.aggressive is False:
                            enemy_list.append(enemy)
                

                while True:
                    investigate_prompt = f"(investigate) What would you like to do? look around, search, pick up, return: "
                    available_actions = ["look around", "search", "pick up", "return"]
                    action = InputHandler.user_input(investigate_prompt, available_actions)
                    print(action)
                    match action[0]:
                        case "look around":
                            if len(interactable_list) == 0 and len(enemy_list) == 0 and len(item_list) == 0:
                                print("You look around the room and see nothing of interest")
                            else:
                                if len(interactable_list) != 0:
                                    print(
                                        f"You look around the room and see a {' ,'.join(interactable_list)}"
                                    )
                                if len(enemy_list) != 0:
                                    print(f"You see some enemies: {' ,'.join([f'{enemy.name} Lvl:{enemy.level}' for enemy in enemy_list])}")
                                if len(item_list) != 0:
                                    print(f"There's some stuff on the floor: {' ,'.join(item_list)}")
                        case "search":
                            try:
                                if action[1]:
                                    for interactable in interactable_list:
                                        if action[1] == interactable.name:
                                            print(f"You search the {interactable.name}...")
                                            if len(interactable.enemies) == 0 and len(interactable.items) == 0:
                                                print("You find nothing")
                                            if len(interactable.enemies) != 0:
                                                enemy = interactable.enemies[random.randrange(0, len(interactable.enemies))]
                                                print(f"You get attacked by: {enemy}!")
                                                ...
                                                # start_attack()???
                                            if len(interactable.items) != 0:
                                                print(f"You find {' ,'.join([f'{interactable.items}'])}")
                                                PlayerHelper.add_items_to_inventory(interactable.items)
                                        else:
                                            print(f"There's no {action[1]} in this room")
                            except IndexError:
                                print("Invalid input")
                                pass

                        case "return":
                            break

                # if action == "check":
                #     inp = input("What would you like to check?: ")
                #     if inp in interactable_name_list:
                #         ...
                        # List stuff thats checkable here
                        # GameobjectHelper.get_gameobject_by_name(inp)
            case "save":
                SaveLoadHandler.save_state(gameobjects)
            case "load":
                gameobjects = GamesaveState.load_state(object_dict)
            case "help":
                print("Here is a list of possible actions:")
                possible_directions = ["north", "south", "west", "east"]
                room_methods = [
                    MapHelper.get_room_to_north_of,
                    MapHelper.get_room_to_south_of,
                    MapHelper.get_room_to_west_of,
                    MapHelper.get_room_to_east_of,
                ]
                for direction, method in zip(possible_directions, room_methods):
                    new_room = method(
                        gameobjects["Player"].current_room, gameobjects["Map"].rooms
                    )
                    if new_room is not None:
                        print(f"- go {direction}: move to the room to the {direction}")
                print("- save: save to this save file")
                print("- load: load the most recent version of this save file")
                print("- help: display this help message")


def start_game():
    try:
        print("Trying to create saves folder...")
        os.mkdir("saves")
    except FileExistsError:
        print("/saves/ folder found: ")
        pass

    if (
        InputHandler.user_input(
            "Would you like to load a previous game or start a new one? (load/new): ",
            ["load", "new"],
        )
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
                user_load = InputHandler.user_input(
                    "Which save file would you like to load? (please enter file name with .json extension): ",
                    savefile_list,
                )
                if user_load in savefile_list:
                    if not os.getcwd().endswith("saves"):
                        os.chdir("saves")

                    return SaveLoadHandler.load_state(user_load)
        else:
            print("No save files found.")
    return None


if __name__ == "__main__":
    main()
