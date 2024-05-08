from Frames.game_play.characters.default import default_character
from Frames.game_play.components.skill_frame import skill_frame
from Frames.game_play.components.hover_frame import hover_frame
from Frames.game_play.components.audio import play_audio
from PIL import Image
from customtkinter import *

class richard_character(default_character):
    def __init__(self, parent: object, width: int, height: int, path_game_over:str, path_wrong_answer: str, character: str, mainmenu_callback, choose_callback):
        super().__init__(parent=parent, width=width, height=height, path_game_over=path_game_over, path_wrong_answer=path_wrong_answer, character=character, main_menu_callback = mainmenu_callback, choose_callback=choose_callback)
        self.character = character
        
        # Skill 1
        self.frame1 = skill_frame(self, 0.1)
        logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/richard/skills_icon/skill_1.jpeg"), dark_image=Image.open("./assets/Characters/richard/skills_icon/skill_1.jpeg"), size=(85, 85))
        self.lbl_skill_1 = CTkLabel(self.frame1, text="", image=logo_skill_1)
        self.lbl_skill_1.pack(padx=7, side="left")
        self.lbl_skill_1.bind("<Button-1>", lambda e: self.skill_1_notif(e))
        self.lbl_skill_1.bind("<Enter>", lambda e: self.on_hover_skill_1(e))
        self.lbl_skill_1.bind("<Leave>", lambda e: self.off_hover_skill_1(e))
        
        # Skill 2
        self.frame2 = skill_frame(self, 0.25)
        self.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/richard/skills_icon/skill_2.jpeg"), dark_image=Image.open("./assets/Characters/richard/skills_icon/skill_2.jpeg"), size=(85, 85))
        self.lbl_skill_2 = CTkLabel(self.frame2, text="", image=self.logo_skill_2)
        self.lbl_skill_2.pack(padx=7, side="left")
        self.lbl_skill_2.bind("<Button-1>", lambda e: self.skill_2_clicked(e))
        self.lbl_skill_2.bind("<Enter>", lambda e: self.on_hover_skill_2(e))
        self.lbl_skill_2.bind("<Leave>", lambda e: self.off_hover_skill_2(e))
        
        # Skills Initialization
        self.skill_1()
        
        
        
    def on_hover_skill_1(self, event):
        self.hover_skill_1 = hover_frame(self, 250, 80, 1, self.character)
        
    def off_hover_skill_1(self, event):
        self.hover_skill_1.destroy()
        
    def on_hover_skill_2(self, event):
        self.hover_skill_2 = hover_frame(self, 400, 90, 2, self.character)
        
    def off_hover_skill_2(self, event):
        self.hover_skill_2.destroy()
        
        
        
        
    
        # this method will re_assign the time_speed of the time_frame module
    def skill_1(self):
        self.time.time_speed = 1200
        
        # visual only
    def skill_1_notif(self, event):
        notif = CTkLabel(self, text=f"Did you know that normal time runs with 1000ms but yours run with 1200ms")
        notif.place(relx=0.5, rely=0.5, anchor="center")
        notif.after(2000, lambda: notif.destroy())

        
    def skill_2_clicked(self, event):
        # setting up the active cooldown
        self.skill_2_remaining_time = 20
        
        # setting up the cooldown or what level will the skill must be available again
        self.cooldown : int = self.guess.current_level + 3
        
        # disabled the skill button
        self.lbl_skill_2.unbind("<Button-1>")
        self.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/richard/skills_icon/skill_2_activate.jpg"), dark_image=Image.open("./assets/Characters/richard/skills_icon/skill_2_activate.jpg"), size=(85, 85))
        self.lbl_skill_2.configure(image=self.logo_skill_2)

        # disable the time from time_frame module
        self.time.active = False
        
        # called out the logic (this is a recursion therefore we have to do it in another method)
        self.skill_activated()

    # this is a recursion if u want to stop the time, then set the attribute of self.skill_2_remaining_time = 0
    def skill_activated(self):
        if self.skill_2_remaining_time:
            self.lbl_skill_2.configure(text=str(self.skill_2_remaining_time), font=("courier", -25, "bold"))
            self.skill_2_remaining_time -= 1
            self.after(1200, self.skill_activated)
            
        # will trigger after the active cooldown
        else:
            self.lbl_skill_2.configure(text="")
            
             # to visually show that the skill is on cooldown
            self.lbl_skill_2.bind("<Button-1>", lambda e: self.skill_2_notif(e))
            
            # run the time again
            self.time.active = True
            self.time.activate_time()
            
    def skill_2_notif(self, event):
        notif = CTkLabel(self, text=f"This skill can be used again on Level {self.cooldown}")
        notif.place(relx=0.5, rely=0.5, anchor="center")
        notif.after(2000, lambda: notif.destroy())