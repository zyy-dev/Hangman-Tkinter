from Frames.game.characters.default import default_character
import random

class renzo_character(default_character):
    def __init__(self, parent: object, width: int, height: int, path_game_over:str, path_wrong_answer: str, character: str):
        super().__init__(parent=parent, width=width, height=height, path_game_over=path_game_over, path_wrong_answer=path_wrong_answer, character=character)
        
    def skill_1(self):
        
        for _ in range(len(self.guess.correct_characters) // 2):
            # getting the correct key
            random_letter = random.choices(list(self.guess.correct_characters))[0].upper()
            
            # using the correct key to call the clicked() method 
            self.keyboard.clicked(self.keyboard.button_address[random_letter])