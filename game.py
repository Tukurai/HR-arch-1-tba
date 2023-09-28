import os

from handlers import SaveLoadHandler, InputHandler
from helpers import MapHelper
from classes import GameobjectData, GamesaveState, Map, Room


def main():
    object_dict = start_game()

    if object_dict is not None:
        gameobjects = GamesaveState.loadstate(object_dict)
    else:
        gameobjects = GameobjectData.init_gameobject_data()

    # Create a new map and add rooms
    game_map = Map(5, 5)
    game_map.add_room(
        Room(id=0, name="Bridge", description="The control center of the spaceship."),
        0,
        0,
    )
    game_map.add_room(
        Room(
            id=1, name="Engine Room", description="A room filled with loud machinery."
        ),
        1,
        0,
    )
    game_map.add_room(
        Room(id=2, name="Cargo Hold", description="A large room for storing cargo."),
        2,
        0,
    )
    game_map.add_room(
        Room(id=3, name="Crew Quarters", description="Where the crew sleeps."), 3, 0
    )
    game_map.add_room(
        Room(
            id=4, name="Medical Bay", description="A clean room with medical equipment."
        ),
        4,
        0,
    )
    game_map.add_room(
        Room(id=5, name="Kitchen", description="A room with cooking equipment."), 0, 1
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
            id=7, name="Bathroom", description="A small room with a shower and toilet."
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

    # Set the player's current room
    for row in game_map.rooms:
        for room in row:
            if room is not None and room.id == 0:  # Assuming id=0 is the starting room
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
        available_actions = ["save", "load", "help"]
        direction_prompts = []

        for direction, method in zip(possible_directions, room_methods):
            new_room = method(gameobjects["Player"].current_room, game_map.rooms)
            if new_room is not None:
                available_actions.insert(0, f"go {direction}")
                direction_prompts.append(f"go {direction}")

        direction_prompts_string = ", ".join(direction_prompts)
        action_prompt = f"What would you like to do? ({direction_prompts_string}, save, load, help): "

        action = InputHandler.user_input(
            action_prompt,
            available_actions,
        )

        match action:
            case "go north":
                new_room = MapHelper.get_room_to_north_of(
                    gameobjects["Player"].current_room, game_map.rooms
                )
                if new_room is not None:
                    gameobjects["Player"].current_room = new_room
                else:
                    print("You cannot go north from here.")
            case "go south":
                new_room = MapHelper.get_room_to_south_of(
                    gameobjects["Player"].current_room, game_map.rooms
                )
                if new_room is not None:
                    gameobjects["Player"].current_room = new_room
                else:
                    print("You cannot go south from here.")
            case "go west":
                new_room = MapHelper.get_room_to_west_of(
                    gameobjects["Player"].current_room, game_map.rooms
                )
                if new_room is not None:
                    gameobjects["Player"].current_room = new_room
                else:
                    print("You cannot go west from here.")
            case "go east":
                new_room = MapHelper.get_room_to_east_of(
                    gameobjects["Player"].current_room, game_map.rooms
                )
                if new_room is not None:
                    gameobjects["Player"].current_room = new_room
                else:
                    print("You cannot go east from here.")
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
                    new_room = method(gameobjects["Player"].current_room, game_map.rooms)
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
