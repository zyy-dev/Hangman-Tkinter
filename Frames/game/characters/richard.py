from Frames.game.characters.default import default_character
from Frames.game.components.skill_frame import skill_frame
from PIL import Image
from customtkinter import *

class richard_character(default_character):
    def __init__(self, parent: object, width: int, height: int, path_game_over:str, path_wrong_answer: str):
        super().__init__(parent=parent, width=width, height=height, path_game_over=path_game_over, path_wrong_answer=path_wrong_answer)
        
        self.frame1 = skill_frame(self, 0.1)
        logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/richard/skills_icon/skill_1.jpeg"), dark_image=Image.open("./assets/Characters/richard/skills_icon/skill_1.jpeg"), size=(85, 85))
        lbl_skill_1 = CTkLabel(self.frame1, text="", image=logo_skill_1)
        lbl_skill_1.pack(padx=7, side="left")
        lbl_skill_1.bind("<Button-1>", self.skill_1)
        
        self.frame2 = skill_frame(self, 0.25)
        logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/richard/skills_icon/skill_2.jpeg"), dark_image=Image.open("./assets/Characters/richard/skills_icon/skill_2.jpeg"), size=(85, 85))
        lbl_skill_2 = CTkLabel(self.frame2, text="", image=logo_skill_2)
        lbl_skill_2.pack(padx=7, side="left")
        lbl_skill_2.bind("<Button-1>", self.skill_2_clicked)
        
        
        self.skill_1(None)
    def skill_1(self, event):
        self.time.time_speed = 1000

    def skill_2_clicked(self, event):
        self.time.active = False
        self.after(5000, self.activate_time_again) 
    
    def activate_time_again(self):
        self.time.active = True
        self.time.activate_time()
