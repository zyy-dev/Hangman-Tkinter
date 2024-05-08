from Frames.game_play.characters.default import default_character
from Frames.game_play.components.skill_frame import skill_frame
from Frames.game_play.components.hover_frame import hover_frame
from Frames.game_play.components.audio import play_audio
from PIL import Image
from customtkinter import *
import random

class zyrus_character(default_character):
    def __init__(self, parent: object, width: int, height: int, path_game_over:str, path_wrong_answer: str, character: str, mainmenu_callback, choose_callback):
        super().__init__(parent=parent, width=width, height=height, path_game_over=path_game_over, path_wrong_answer=path_wrong_answer, character=character, main_menu_callback = mainmenu_callback, choose_callback=choose_callback)
        self.character = character
        
        # Skill 1
        self.frame1 = skill_frame(self, 0.1)
        self.logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/zyrus/skills_icon/skill_1.jpg"), dark_image=Image.open("./assets/Characters/zyrus/skills_icon/skill_1.jpg"), size=(85, 85))
        self.lbl_skill_1 = CTkLabel(self.frame1, text="", image=self.logo_skill_1)
        self.lbl_skill_1.pack(padx=7, side="left")
        self.lbl_skill_1.bind("<Button-1>", lambda e: self.skill_1(e))
        self.lbl_skill_1.bind("<Enter>", lambda e: self.on_hover_skill_1(e))
        self.lbl_skill_1.bind("<Leave>", lambda e: self.off_hover_skill_1(e))
        # Skill 2
        self.frame2 = skill_frame(self, 0.25)
        self.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/zyrus/skills_icon/skill_2.jpg"), dark_image=Image.open("./assets/Characters/zyrus/skills_icon/skill_2.jpg"), size=(85, 85))
        self.lbl_skill_2 = CTkLabel(self.frame2, text="", image=self.logo_skill_2)
        self.lbl_skill_2.pack(padx=7, side="left")
        self.lbl_skill_2.bind("<Button-1>", lambda e: self.skill_2(e))
        self.lbl_skill_2.bind("<Enter>", lambda e: self.on_hover_skill_2(e))
        self.lbl_skill_2.bind("<Leave>", lambda e: self.off_hover_skill_2(e))
        
        self.skill_1_state = False
        self.skill_2_state = False
        self.cooldown = False
        
    def on_hover_skill_1(self, event):
        self.hover_skill_1 = hover_frame(self, 400, 100, 1, self.character)
        
    def off_hover_skill_1(self, event):
        self.hover_skill_1.destroy()
        
    def on_hover_skill_2(self, event):
        self.hover_skill_2 = hover_frame(self, 400, 90, 2, self.character)
        
    def off_hover_skill_2(self, event):
        self.hover_skill_2.destroy()
            

    def skill_1(self, event):
        # set this True to make the pressed keys to dont reflect with the count of mistakes
        self.skill_1_state = True
        
        # set the skill's cooldown
        self.cooldown: int = self.guess.current_level + 3
        
        # algorithm to disable wrong keys from the keybaord module
        available_characters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        for char in available_characters.copy():
            if char in self.keyboard.key_already_pressed:
                available_characters.remove(char)
            if char in self.guess.word_to_guess:
                available_characters.remove(char)
        for _ in range(5):
            random_letter = random.choice(available_characters)[0]
            self.keyboard.clicked(self.keyboard.button_address[random_letter])
            available_characters.remove(random_letter)
            
        # disabled the skill button
        self.lbl_skill_1.unbind("<Button-1>")
        self.logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/zyrus/skills_icon/skill_1_activate.jpg"), dark_image=Image.open("./assets/Characters/zyrus/skills_icon/skill_1_activate.jpg"), size=(85, 85))
        self.lbl_skill_1.configure(image=self.logo_skill_1)
        
        # setting the atttribute back to False again because we only want this skill ton be triggered once
        # or to be triggered again under the conditions in keyboard module   
        self.skill_1_state = False
        
        # to visually show that the skill is on cooldown
        self.lbl_skill_1.bind("<Button-1>", lambda e: self.skill_1_notif(e))
        
        # skill's sound effect
        play_audio.skill(self.character, "1")
    def skill_1_notif(self, event):
        notif = CTkLabel(self, text=f"This skill can be used again on Level {self.cooldown}")
        notif.place(relx=0.5, rely=0.5, anchor="center")
        notif.after(2000, lambda: notif.destroy())
        

        
    def skill_2(self, event):
        self.skill_2_state = True
        
        # disabled the skill button
        self.lbl_skill_2.unbind("<Button-1>")
        self.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/zyrus/skills_icon/skill_2_activate.jpg"), dark_image=Image.open("./assets/Characters/zyrus/skills_icon/skill_2_activate.jpg"), size=(85, 85))
        self.lbl_skill_2.configure(image=self.logo_skill_2)
        
        # procede to the next Level using the reset() method of the keyboard module
        self.keyboard.reset()
        
        # to visually show that the skill is on cooldown
        self.lbl_skill_2.bind("<Button-1>", lambda e: self.skill_2_notif(e))
        
        # skill's sound effect
        play_audio.skill(self.character, "2")
        
    def skill_2_notif(self, event):
        notif = CTkLabel(self, text=f"This skill can only be used once")
        notif.place(relx=0.5, rely=0.5, anchor="center")
        
        # destroy the notification after 2 seconds
        notif.after(2000, lambda: notif.destroy())