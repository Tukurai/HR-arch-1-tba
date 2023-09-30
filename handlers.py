# handlers.py

import json
import os
import time


class InputHandler:
    @staticmethod
    def user_input(message, choices=None):
        while True:
            StoryOutputHandler.story_output(message, 15, False)
            user_input = input()
            if choices is None or user_input in choices:
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