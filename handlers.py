# handlers.py

import msvcrt
import sys
import time


class InputHandler:
    @staticmethod
    def user_input(message, choices=None):
        while True:
            StoryOutputHandler.story_output(message, 15, False)
            user_input = input()
            if choices is None or user_input.lower() in [choice.lower() for choice in choices]:
                return user_input
            else:
                StoryOutputHandler.story_output(
                    f"Invalid input, your choices are: ({', '.join(choices)})", 15
                )

    @staticmethod
    def user_keypress(message, key=None, delay=50, newline=True):
        StoryOutputHandler.story_output(message, delay, newline)
        while True:
            pressed = msvcrt.getch().decode().lower()
            if key is None or pressed == key.lower():
                return
            sys.stdout.write("\b")
        return


class StoryOutputHandler:
    @staticmethod
    def story_output(message, delay=50, newline=True):
        for letter in message:
            print(letter, end="", flush=True)
            time.sleep(delay / 1000)
        if newline:
            print()
