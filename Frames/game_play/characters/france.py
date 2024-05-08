from Frames.game_play.characters.default import default_character
from Frames.game_play.components.skill_frame import skill_frame
from Frames.game_play.components.hover_frame import hover_frame
from PIL import Image
from customtkinter import *

class france_character(default_character):
    def __init__(self, parent: object, width: int, height: int, path_game_over:str, path_wrong_answer: str, character: str, mainmenu_callback, choose_callback):
        super().__init__(parent=parent, width=width, height=height, path_game_over=path_game_over, path_wrong_answer=path_wrong_answer, character=character, main_menu_callback = mainmenu_callback, choose_callback=choose_callback)
        self.character = character
        
        # Skill 1
        self.frame1 = skill_frame(self, 0.1)
        self.logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/france/skills_icon/skill_1.png"), dark_image=Image.open("./assets/Characters/france/skills_icon/skill_1.png"), size=(85, 85))
        self.lbl_skill_1 = CTkLabel(self.frame1, text="", image=self.logo_skill_1)
        self.lbl_skill_1.pack(padx=7, side="left")
        self.lbl_skill_1.bind("<Button-1>", lambda e: self.skill_1_notif(e))
        self.lbl_skill_1.bind("<Enter>", lambda e: self.on_hover_skill_1(e))
        self.lbl_skill_1.bind("<Leave>", lambda e: self.off_hover_skill_1(e))
        
        # Skill 2
        self.frame2 = skill_frame(self, 0.25)
        self.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/france/skills_icon/skill_2.png"), dark_image=Image.open("./assets/Characters/france/skills_icon/skill_2.png"), size=(85, 85))
        self.lbl_skill_2 = CTkLabel(self.frame2, text="", image=self.logo_skill_2)
        self.lbl_skill_2.pack(padx=7, side="left")
        self.lbl_skill_2.bind("<Button-1>", lambda e: self.skill_2(e))
        self.lbl_skill_2.bind("<Enter>", lambda e: self.on_hover_skill_2(e))
        self.lbl_skill_2.bind("<Leave>", lambda e: self.off_hover_skill_2(e))
        
        # attributes initialization
        self.skill_2_remaining_time = 3
        self.triggered = 0
        self.skill_1_name = "Extra Rice pa po"
        self.skill_2_state = False
        
        
    def on_hover_skill_1(self, event):
        self.hover_skill_1 = hover_frame(self, 400, 100, 1, self.character)
        
    def off_hover_skill_1(self, event):
        self.hover_skill_1.destroy()
        
    def on_hover_skill_2(self, event):
        self.hover_skill_2 = hover_frame(self, 400, 105, 2, self.character)
        
    def off_hover_skill_2(self, event):
        self.hover_skill_2.destroy()
        
        
        # passive skill
        # this method will be called under certain condition in the time_frame module
    def skill_1(self):
        # to make sure that this skill will only be triggered once
        self.triggered += 1
        if self.triggered == 1:
            # 20 seconds will be added from the time_frame module
            self.time.seconds += 20
            
            # visually showing that the skill has been activated
            notice = CTkLabel(self, text=f"Passive Skill Activated: {self.skill_1_name}")
            notice.place(relx=0.5, rely=0.5, anchor="center")
            notice.after(2000, lambda: notice.destroy())
            
            self.logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/france/skills_icon/skill_1_activate.jpg"), dark_image=Image.open("./assets/Characters/france/skills_icon/skill_1_activate.jpg"), size=(85, 85))
            self.lbl_skill_1.configure(image=self.logo_skill_1)
            
    def skill_1_notif(self, event):
        # Just incase if the user is dumb enough to realize that passice skill doesn't need to be clicked
        notif = CTkLabel(self, text=f"This is a passive skill")
        notif.place(relx=0.5, rely=0.5, anchor="center")
        notif.after(2000, lambda: notif.destroy())
            
    def skill_2(self, event):
        # disabled the skill button
        self.lbl_skill_2.unbind("<Button-1>")
        self.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/france/skills_icon/skill_2_activate.png"), dark_image=Image.open("./assets/Characters/france/skills_icon/skill_2_activate.png"), size=(85, 85))
        self.lbl_skill_2.configure(image=self.logo_skill_2)
        
        # called out the logic (this is a recursion therefore we have to do it in another method)
        self.skill_activated()
        
        
    # this is a recursion if u want to stop the time, then set the attribute of self.skill_2_remaining_time = 0
    def skill_activated(self):
        if self.skill_2_remaining_time:
            #  this will make the program to neglect the wrong keys from the keyboard module
            self.skill_2_state = True
            
            # visually showing the active cooldown of the skill
            self.lbl_skill_2.configure(text=str(self.skill_2_remaining_time), font=("courier", -25, "bold"))
            
            # recursion
            self.skill_2_remaining_time -= 1
            self.after(1000, self.skill_activated)
            
        # will trigger after the active cooldown
        else:
            self.skill_2_state = False
            self.lbl_skill_2.configure(text="")
            self.lbl_skill_2.bind("<Button-1>", lambda e: self.skill_2_notif(e))
            
    # new bind method once the skill 2 is used
    def skill_2_notif(self, event):
        notif = CTkLabel(self, text="This skill can only be used once")
        notif.place(relx=0.5, rely=0.5, anchor="center")
        notif.after(2000, lambda: notif.destroy())
        