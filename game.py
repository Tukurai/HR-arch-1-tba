# game.py

import os
import random

from handlers import InputHandler, StoryOutputHandler
from helpers import MapHelper
from classes import GameState


def main():
    game_state = GameState(
        player_name=InputHandler.user_input(
            f"Your ship has crashed on a planet, you lost your memories.\nWhat is the name on your uniform?: "
        )
    )
    StoryOutputHandler.story_output(f"You pick yourself up from the ground...", 100)
    StoryOutputHandler.story_output(f"There's a warning on your visor: ", 100, False)
    StoryOutputHandler.story_output(f"WARNING DANGEROUS ATMOSPHERE DETECTED!", 25)
    InputHandler.user_keypress(f"Press C gather yourself, and seek shelter.", "C")
    StoryOutputHandler.story_output(
        f"You quickly take shelter in a nearby abandoned freighter. You decide to search for parts to fix your spaceship."
    )
    StoryOutputHandler.story_output("The bridge door slams behind you. There's no going back now.")
    InputHandler.user_keypress("Press any key to continue...")

    # Set the player's current room to starting room
    for row in game_state.map.rooms:
        for room in row:
            if room is not None and room.id == 0:  # Assuming id=0 is the starting room
                game_state.player.current_room = room
                break

    while True:
        os.system("cls")
        StoryOutputHandler.story_output(
            f"You are currently in the {game_state.player.current_room.name}."
        )

        current_room = game_state.player.current_room

        possible_directions = ["north", "south", "west", "east"]

        room_methods = [
            MapHelper.get_room_to_north_of,
            MapHelper.get_room_to_south_of,
            MapHelper.get_room_to_west_of,
            MapHelper.get_room_to_east_of,
        ]

        action_dictionary = {
            "go north": "Go to the room north of this room.",
            "go east": "Go to the room east of this room.",
            "go south": "Go to the room south of this room.",
            "go west": "Go to the room west of this room.",
            "investigate": "enter the investigate sub-menu",
            "inventory": "enter the inventory sub-menu",
            "pick up": "pick up the items you saw while looking around.",
            "attack": "enter the attack sub-menu",
            "help": "Displays this menu.",
        }

        available_actions = [
            "investigate",
            "inventory",
            "help",
        ]

        for direction, method in zip(possible_directions, room_methods):
            new_room = method(current_room, game_state.map.rooms)
            if new_room is not None:
                available_actions.insert(0, f"go {direction}")

        if current_room.was_looked_around:
            if any(enemy_list):
                available_action.append("attack")

        action_prompt = f"What would you like to do? ({', '.join(available_actions)}): "

        action = InputHandler.user_input(action_prompt, available_actions)

        match action:
            case "go north":
                new_room = MapHelper.get_room_to_north_of(
                    game_state.player.current_room, game_state.map.rooms
                )
                if new_room is not None:
                    game_state.player.current_room = new_room
                else:
                    StoryOutputHandler.story_output("You cannot go north from here.")
            case "go south":
                new_room = MapHelper.get_room_to_south_of(
                    game_state.player.current_room, game_state.map.rooms
                )
                if new_room is not None:
                    game_state.player.current_room = new_room
                else:
                    StoryOutputHandler.story_output("You cannot go south from here.")
            case "go west":
                new_room = MapHelper.get_room_to_west_of(
                    game_state.player.current_room, game_state.map.rooms
                )
                if new_room is not None:
                    game_state.player.current_room = new_room
                else:
                    StoryOutputHandler.story_output("You cannot go west from here.")
            case "go east":
                new_room = MapHelper.get_room_to_east_of(
                    game_state.player.current_room, game_state.map.rooms
                )
                if new_room is not None:
                    game_state.player.current_room = new_room
                else:
                    StoryOutputHandler.story_output("You cannot go east from here.")

            case "investigate":
                item_name_list = [item.name for item in current_room.items]

                interactable_list = current_room.interactables
                interactable_name_list = [
                    interactable.name for interactable in current_room.interactables
                ]

                enemy_list = current_room.enemies
                enemy_name_list = [enemy.name for enemy in enemy_list]

                while True:
                    sub_actions = ["look around", "return"]

                    if current_room.was_looked_around:
                        if any(current_room.items):
                            sub_actions.append("pick up")

                        if any(interactable_list):
                            sub_actions.append("search")

                    sub_prompt = f"({action}) What would you like to do? ({', '.join(sub_actions)}): "
                    sub_action = InputHandler.user_input(sub_prompt, sub_actions)
                    match sub_action:
                        case "look around":
                            current_room.was_looked_around = True

                            result = []

                            if len(interactable_list) != 0:
                                result.append(
                                    f"You look around the room and see a {' ,'.join(interactable_name_list)}"
                                )

                            if len(enemy_list) != 0:
                                result.append(
                                    f"You see some enemies: {' ,'.join([f'{enemy.name} Lvl:{enemy.level}' for enemy in enemy_list])}"
                                )

                            if len(current_room.items) != 0:
                                result.append(
                                    f"There's some stuff on the floor: {' ,'.join(item_name_list)}"
                                )

                            if len(result) == 0:
                                result.append(
                                    "You look around the room and see nothing of interest"
                                )

                            StoryOutputHandler.story_output("\n".join(result))
                        case "pick up":
                            if len(current_room.items) != 0:
                                StoryOutputHandler.story_output(
                                    f"You pick up {' ,'.join([f'{item_name_list}'])}"
                                )
                                game_state.player.inventory_add(current_room.items)
                                current_room.items = []

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

                                interactable_items_name_list = [
                                   item.name for item in interactable.items
                                ]

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
                                        f"You pick up {' ,'.join([f'{interactable_items_name_list}'])}"
                                    )
                                    game_state.player.inventory_add(interactable.items)
                                    interactable.items = []

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
                inventory_name_list = [
                    f"- {inventory_obj.name}: {inventory_obj.description}\n"
                    for inventory_obj in game_state.player.inventory
                ]

                StoryOutputHandler.story_output(
                    f"Your inventory contains:\n{''.join(inventory_name_list)}"
                )

                InputHandler.user_keypress("Press any key to continue...")
            # case "attack":
            case "help":
                print("Here is a list of possible actions:")

                for available_action in available_actions:
                    StoryOutputHandler.story_output(
                        f"- {available_action}: {action_dictionary[available_action]}",
                        10,
                    )

                InputHandler.user_keypress("Press any key to continue...")


if __name__ == "__main__":
    main()
