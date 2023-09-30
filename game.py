# game.py

import os
import random

from handlers import SaveLoadHandler, InputHandler, StoryOutputHandler
from helpers import MapHelper, GameobjectHelper, PlayerHelper
from classes import GameobjectData, GamesaveState, Map, Room


def main():
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
        StoryOutputHandler.story_output(
            f"You are currently in the {gameobjects['Player'].current_room.name}."
        )

        current_room = gameobjects["Player"].current_room

        possible_directions = ["north", "south", "west", "east"]
        
        room_methods = [
            MapHelper.get_room_to_north_of,
            MapHelper.get_room_to_south_of,
            MapHelper.get_room_to_west_of,
            MapHelper.get_room_to_east_of,
        ]

        available_actions = [
            "investigate",
            "inventory",
            "attack",
            "save",
            "load",
            "help",
        ]

        for direction, method in zip(possible_directions, room_methods):
            new_room = method(current_room, gameobjects["Map"].rooms)
            if new_room is not None:
                available_actions.insert(0, f"go {direction}")

        action_prompt = f"What would you like to do? ({', '.join(available_actions)}): "

        action = InputHandler.user_input(
            action_prompt,
            available_actions
        )

        match action:
            case "go north":
                new_room = MapHelper.get_room_to_north_of(
                    gameobjects["Player"].current_room, gameobjects["Map"].rooms
                )
                if new_room is not None:
                    gameobjects["Player"].current_room = new_room
                else:
                    StoryOutputHandler.story_output("You cannot go north from here.")
            case "go south":
                new_room = MapHelper.get_room_to_south_of(
                    gameobjects["Player"].current_room, gameobjects["Map"].rooms
                )
                if new_room is not None:
                    gameobjects["Player"].current_room = new_room
                else:
                    StoryOutputHandler.story_output("You cannot go south from here.")
            case "go west":
                new_room = MapHelper.get_room_to_west_of(
                    gameobjects["Player"].current_room, gameobjects["Map"].rooms
                )
                if new_room is not None:
                    gameobjects["Player"].current_room = new_room
                else:
                    StoryOutputHandler.story_output("You cannot go west from here.")
            case "go east":
                new_room = MapHelper.get_room_to_east_of(
                    gameobjects["Player"].current_room, gameobjects["Map"].rooms
                )
                if new_room is not None:
                    gameobjects["Player"].current_room = new_room
                else:
                    StoryOutputHandler.story_output("You cannot go east from here.")

            case "investigate":
                item_list = current_room.items
                interactable_list = current_room.interactables
                interactable_name_list = [
                    interactable.name for interactable in current_room.interactables
                ]
                enemy_list = current_room.enemies

                while True:
                    sub_actions = ["look around", "return"]
                    if any(interactable_name_list):
                        sub_actions.append("search")

                    sub_prompt = f"({action}) What would you like to do? ({', '.join(sub_actions)}): "
                    sub_action = InputHandler.user_input(sub_prompt, sub_actions)
                    match sub_action:
                        case "look around":
                            result = []

                            if len(interactable_list) != 0:
                                result.append(
                                    f"You look around the room and see a {' ,'.join(interactable_list)}"
                                )

                            if len(enemy_list) != 0:
                                result.append(
                                    f"You see some enemies: {' ,'.join([f'{enemy.name} Lvl:{enemy.level}' for enemy in enemy_list])}"
                                )

                            if len(item_list) != 0:
                                result.append(
                                    f"There's some stuff on the floor: {' ,'.join(item_list)}"
                                )

                            if len(result) == 0:
                                result.append(
                                    "You look around the room and see nothing of interest"
                                )

                            StoryOutputHandler.story_output("\n".join(result))
                        case "search":
                            search_prompt = f"({sub_action}) Which object? ({', '.join(interactable_name_list)}): "
                            search_action = InputHandler.user_input(
                                search_prompt, interactable_name_list
                            )

                            interactable = next(
                                (
                                    interactable
                                    for interactable in interactable_list
                                    if interactable.name == search_action
                                ),
                                None,
                            )
                            if interactable is not None:
                                result = []

                                StoryOutputHandler.story_output(
                                    f"You search the {interactable.name}...", 100
                                )

                                if len(interactable.enemies) != 0:
                                    enemy = interactable.enemies[
                                        random.randrange(0, len(interactable.enemies))
                                    ]
                                    enemy.aggresive = True
                                    current_room.enemies.append(enemy)

                                    result.append(f"You get attacked by: {enemy.name}!")

                                if len(interactable.items) != 0:
                                    result.append(
                                        f"You pick up {' ,'.join([f'{interactable.items}'])}"
                                    )
                                    PlayerHelper.add_items_to_inventory(
                                        interactable.items
                                    )

                                if len(result) == 0:
                                    result.append("You find nothing")

                                StoryOutputHandler.story_output("\n".join(result))
                            else:
                                StoryOutputHandler.story_output(
                                    f"There's no {search_action} in this room"
                                )
                        case "return":
                            break

            case "inventory":
                StoryOutputHandler.story_output(
                    f"Your inventory contains:\n{', '.join(gameobjects['Player'].inventory)}"
                )
            # case "attack":
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
    if not os.path.exists("saves"):
        os.makedirs("saves")

    savefile_list = []
    for root, dirs, files in os.walk("saves"):
        for file in files:
            if file.endswith(".json"):
                file_name = file.replace(".json", "")
                savefile_list.append(file_name.lower())

    if (
        len(savefile_list) == 0
        or InputHandler.user_input(
            "Would you like to load a previous game or start a new one? (load/new): ",
            ["load", "new"],
        )
        == "new"
    ):
        return None

    user_load = InputHandler.user_input(
        f"Which save file would you like to load? ({', '.join(savefile_list)}): ",
        savefile_list,
    )
    return SaveLoadHandler.load_state(user_load)


if __name__ == "__main__":
    main()
