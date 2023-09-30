# handlers.py

import json
import os
import time


class SaveLoadHandler:
    @staticmethod
    def load_state(file_name):
        if not os.getcwd().endswith("saves"):
            os.chdir("saves")

        with open(f"{file_name}.json", "r") as json_file:
            return json.load(json_file)

    @staticmethod
    def save_state(gameobjects):
        file_name = f"{gameobjects['Player'].name.lower()}.json"

        if not os.getcwd().endswith("saves"):
            os.chdir("saves")

        with open(file_name, "w") as file:
            print("Saving game...")
            json.dump(gameobjects, file, default=lambda o: o.__dict__)
            print("Game saved successfully")


class InputHandler:
    @staticmethod
    def user_input(message, choices):
        while True:
            StoryOutputHandler.story_output(message, 15, False)
            user_input = input()
            if user_input in choices:
                return user_input
            else:
                StoryOutputHandler.story_output(
                    f"Invalid input, your choices are: ({', '.join(choices)})", 15
                )


class StoryOutputHandler:
    @staticmethod
    def story_output(message, delay=50, newline=True):
        for letter in message:
            print(letter, end="", flush=True)
            time.sleep(delay / 1000)
        if newline:
            print()
