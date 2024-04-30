from Frames.game.characters.default import default_character
from Frames.game.components.skill_frame import skill_frame
from PIL import Image
from customtkinter import *

class richard_character(default_character):
    def __init__(self, parent: object, width: int, height: int, path_game_over:str, path_wrong_answer: str, character: str):
        super().__init__(parent=parent, width=width, height=height, path_game_over=path_game_over, path_wrong_answer=path_wrong_answer, character=character)
        
        self.frame1 = skill_frame(self, 0.1)
        logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/richard/skills_icon/skill_1.jpeg"), dark_image=Image.open("./assets/Characters/richard/skills_icon/skill_1.jpeg"), size=(85, 85))
        lbl_skill_1 = CTkLabel(self.frame1, text="", image=logo_skill_1)
        lbl_skill_1.pack(padx=7, side="left")
        
        self.frame2 = skill_frame(self, 0.25)
        self.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/richard/skills_icon/skill_2.jpeg"), dark_image=Image.open("./assets/Characters/richard/skills_icon/skill_2.jpeg"), size=(85, 85))
        self.lbl_skill_2 = CTkLabel(self.frame2, text="", image=self.logo_skill_2)
        self.lbl_skill_2.pack(padx=7, side="left")
        self.lbl_skill_2.bind("<Button-1>", lambda e: self.skill_2_clicked(e))
        
        self.skill_2_name = "tap tap tap"
        
        self.skill_1()
    def skill_1(self):
        self.time.time_speed = 2000

    def skill_2_clicked(self, event):
        self.cooldown : int = self.guess.current_level + 2
        self.lbl_skill_2.unbind("<Button-1>")
        self.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/richard/skills_icon/skill_2_activate.jpg"), dark_image=Image.open("./assets/Characters/richard/skills_icon/skill_2_activate.jpg"), size=(85, 85))
        self.lbl_skill_2.configure(image=self.logo_skill_2)
        print(self.time.active)
        self.time.active = False
        print(self.time.active)
        self.skill_activated()

        
    def skill_activated(self, remaining_time = 20):
        if remaining_time:
            self.lbl_skill_2.configure(text=str(remaining_time), font=("courier", -25, "bold"))
            self.after(1200, lambda: self.skill_activated(remaining_time - 1))
        else:
            self.lbl_skill_2.configure(text="")
            self.frame2.configure(border_color="red")
            
            self.lbl_skill_2.bind("<Button-1>", lambda e: self.skill_2_notif(e))
            
            # run the time again
            self.time.active = True
            self.time.activate_time()
            
    def skill_2_notif(self, event):
        notif = CTkLabel(self, text=f"{self.skill_2_name} is on cooldown...")
        notif.place(relx=0.5, rely=0.5, anchor="center")
    
        notif.after(2000, lambda: notif.configure(text=""))