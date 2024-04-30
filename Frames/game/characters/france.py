from Frames.game.characters.default import default_character
from Frames.game.components.skill_frame import skill_frame
from PIL import Image
from customtkinter import *
import random

class france_character(default_character):
    def __init__(self, parent: object, width: int, height: int, path_game_over:str, path_wrong_answer: str, character: str):
        super().__init__(parent=parent, width=width, height=height, path_game_over=path_game_over, path_wrong_answer=path_wrong_answer, character=character)

        self.frame1 = skill_frame(self, 0.1)
        logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/france/skills_icon/skill_1.png"), dark_image=Image.open("./assets/Characters/france/skills_icon/skill_1.png"), size=(85, 85))
        lbl_skill_1 = CTkLabel(self.frame1, text="", image=logo_skill_1)
        lbl_skill_1.pack(padx=7, side="left")
        
        self.frame2 = skill_frame(self, 0.25)
        self.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/france/skills_icon/skill_2.png"), dark_image=Image.open("./assets/Characters/france/skills_icon/skill_2.png"), size=(85, 85))
        self.lbl_skill_2 = CTkLabel(self.frame2, text="", image=self.logo_skill_2)
        self.lbl_skill_2.pack(padx=7, side="left")
        self.lbl_skill_2.bind("<Button-1>", lambda e: self.skill_2(e))
        self.skill_2_remaining_time = 3
        self.triggered = 0
        self.skill_2_name = "Diwata Pares"
    def skill_1(self):
        # to make sure that this skill will only be triggered once
        self.triggered += 1
        if self.triggered == 1:
            self.time.seconds += 20
    
    def skill_2(self, event):
        self.lbl_skill_2.unbind("<Button-1>")
        self.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/france/skills_icon/skill_2_activate.png"), dark_image=Image.open("./assets/Characters/france/skills_icon/skill_2_activate.png"), size=(85, 85))
        self.lbl_skill_2.configure(image=self.logo_skill_2)
        
        self.skill_activated()
        
        
    # this is a recursion if u want to stop the time, then set the attribute of self.skill_2_remaining_time = 0
    def skill_activated(self):
        if self.skill_2_remaining_time:
            self.keyboard.france_skill = True
            self.lbl_skill_2.configure(text=str(self.skill_2_remaining_time), font=("courier", -25, "bold"))
            self.skill_2_remaining_time -= 1
            self.after(1000, self.skill_activated)
        else:
            self.keyboard.france_skill = False
            self.lbl_skill_2.configure(text="")
            self.lbl_skill_2.bind("<Button-1>", lambda e: self.skill_2_notif(e))
            
            
    def skill_2_notif(self, event):
        notif = CTkLabel(self, text=f"{self.skill_2_name} can only be used once")
        notif.place(relx=0.5, rely=0.5, anchor="center")

        notif.after(2000, lambda: notif.destroy())
        