from Frames.game_play.characters.default import default_character
from Frames.game_play.components.skill_frame import skill_frame
from Frames.game_play.components.hover_frame import hover_frame
from PIL import Image
from customtkinter import *
import random

class renzo_character(default_character):
    def __init__(self, parent: object, width: int, height: int, path_game_over:str, path_wrong_answer: str, character: str, mainmenu_callback, choose_callback):
        super().__init__(parent=parent, width=width, height=height, path_game_over=path_game_over, path_wrong_answer=path_wrong_answer, character=character, main_menu_callback = mainmenu_callback, choose_callback=choose_callback)
        self.character = character
        
        # Skill 1
        self.frame1 = skill_frame(self, 0.1)
        self.logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/renzo/skills_icon/skill_1.jpg"), dark_image=Image.open("./assets/Characters/renzo/skills_icon/skill_1.jpg"), size=(85, 85))
        self.lbl_skill_1 = CTkLabel(self.frame1, text="", image=self.logo_skill_1)
        self.lbl_skill_1.pack(padx=7, side="left")
        self.lbl_skill_1.bind("<Button-1>", lambda e: self.skill_1(e))
        self.lbl_skill_1.bind("<Enter>", lambda e: self.on_hover_skill_1(e))
        self.lbl_skill_1.bind("<Leave>", lambda e: self.off_hover_skill_1(e))
        
        # Skill 2
        self.frame2 = skill_frame(self, 0.25)
        self.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/renzo/skills_icon/skill_2.jpg"), dark_image=Image.open("./assets/Characters/renzo/skills_icon/skill_2.jpg"), size=(85, 85))
        self.lbl_skill_2 = CTkLabel(self.frame2, text="", image=self.logo_skill_2)
        self.lbl_skill_2.pack(padx=7, side="left")
        self.lbl_skill_2.bind("<Button-1>", lambda e: self.skill_2(e))
        self.lbl_skill_2.bind("<Enter>", lambda e: self.on_hover_skill_2(e))
        self.lbl_skill_2.bind("<Leave>", lambda e: self.off_hover_skill_2(e))
        
        # Initialization
        self.skill_1_state = False
        self.skill_2_state = False
        self.cooldown1 = False
        self.cooldown2 = False
        
    def on_hover_skill_1(self, event):
        self.hover_skill_1 = hover_frame(self, 400, 90, 1, self.character)
        
    def off_hover_skill_1(self, event):
        self.hover_skill_1.destroy()
        
    def on_hover_skill_2(self, event):
        self.hover_skill_2 = hover_frame(self, 400, 100, 2, self.character)
        
    def off_hover_skill_2(self, event):
        self.hover_skill_2.destroy()
    
    def skill_1(self, event):
        # this will retain the current level by manipulating the guess module
        self.skill_1_state = True
        
        # this will make everything to procede to the next level, but due to the self.skill_1_state, the current_level will retain
        self.keyboard.reset()
        
        # setting up the cooldown or what level will the skill must be available again
        self.cooldown1 = self.guess.current_level + 2
            
        # disabled the skill button
        self.lbl_skill_1.unbind("<Button-1>")
        self.logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/renzo/skills_icon/skill_1_activate.jpg"), dark_image=Image.open("./assets/Characters/renzo/skills_icon/skill_1_activate.jpg"), size=(85, 85))
        self.lbl_skill_1.configure(image=self.logo_skill_1)
        
        # to visually show that the skill is on cooldown
        self.lbl_skill_1.bind("<Button-1>", lambda e: self.skill_1_notif(e))
            
    def skill_1_notif(self, event):
        notif = CTkLabel(self, text=f"This skill can be used again on Level {self.cooldown1}")
        notif.place(relx=0.5, rely=0.5, anchor="center")
        notif.after(2000, lambda: notif.destroy())
        
        
        
    def skill_2(self, event):
        # this will retain the current level by manipulating the keyboard module
        self.skill_2_state = True
        
        self.cooldown2 = self.guess.current_level + 4
        for _ in range(len(self.guess.correct_characters) // 2):
            # getting the correct key
            random_letter = random.choices(list(self.guess.correct_characters))[0].upper()
            
            # using the correct key to call the clicked() method 
            self.keyboard.clicked(self.keyboard.button_address[random_letter])
        if self.keyboard.correct == len(set(self.guess.word_to_guess)):
            self.keyboard.points.append((self.keyboard.time_callback.seconds * self.guess.current_level)//2)
        # disabled the skill button
        self.lbl_skill_2.unbind("<Button-1>")
        self.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/renzo/skills_icon/skill_2_activate.jpg"), dark_image=Image.open("./assets/Characters/renzo/skills_icon/skill_2_activate.jpg"), size=(85, 85))
        self.lbl_skill_2.configure(image=self.logo_skill_2)
        
        # to visually show that the skill is on cooldown
        self.lbl_skill_2.bind("<Button-1>", lambda e: self.skill_2_notif(e))
            
    def skill_2_notif(self, event):
        notif = CTkLabel(self, text=f"This skill can be used again on Level {self.cooldown2}")
        notif.place(relx=0.5, rely=0.5, anchor="center")
        notif.after(2000, lambda: notif.destroy())