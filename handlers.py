# handlers.py

import json  
import os  
  
class SaveLoadHandler:  
    @staticmethod  
    def load_state(file_name):  
        with open(file_name, "r") as json_file:  
            return json.load(json_file)  
  
    @staticmethod  
    def save_state(gameobjects):  
        file_name = f"{gameobjects['Player'].name}-save.json"  
  
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
            user_input = input(message)  
            if user_input in choices:  
                return user_input  
            else:  
                print("Invalid input. Please try again.")  
