from Frames.game.characters.default import default_character
from Frames.game.components.skill_frame import skill_frame
from PIL import Image
from customtkinter import *
import random

class allan_character(default_character):
    def __init__(self, parent: object, width: int, height: int, path_game_over:str, path_wrong_answer: str, character: str):
        super().__init__(parent=parent, width=width, height=height, path_game_over=path_game_over, path_wrong_answer=path_wrong_answer, character=character)
        self.skill_2_active = False
        
        self.frame1 = skill_frame(self, 0.1)
        logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/allan/skills_icon/skill_1.png"), dark_image=Image.open("./assets/Characters/allan/skills_icon/skill_1.png"), size=(85, 85))
        lbl_skill_1 = CTkLabel(self.frame1, text="", image=logo_skill_1)
        lbl_skill_1.pack(padx=7, side="left")
        
        self.frame2 = skill_frame(self, 0.25)
        logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/allan/skills_icon/skill_2.png"), dark_image=Image.open("./assets/Characters/allan/skills_icon/skill_2.png"), size=(85, 85))
        lbl_skill_2 = CTkLabel(self.frame2, text="", image=logo_skill_2)
        lbl_skill_2.pack(padx=7, side="left")
        lbl_skill_2.bind("<Button-1>", self.skill_2)
        
    def skill_1(self):
        random_letter = random.choices(self.guess.word_to_guess)[0].upper()
        self.keyboard.clicked(self.keyboard.button_address[random_letter])
        
    def skill_2(self, event):
        self.skill_2_active = True