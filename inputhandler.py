class InputHandler:  
    @staticmethod  
    def user_input(message, choices):  
        while True:  
            user_input = input(message)  
            if user_input in choices:  
                return user_input  
            else:  
                print("Invalid input. Please try again.")  
