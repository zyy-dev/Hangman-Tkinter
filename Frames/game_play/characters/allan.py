from Frames.game_play.characters.default import default_character
from Frames.game_play.components.skill_frame import skill_frame
from Frames.game_play.components.hover_frame import hover_frame
from Frames.game_play.components.audio import play_audio
from PIL import Image
from customtkinter import CTkImage, CTkLabel
import random

class allan_character(default_character):
    def __init__(self, parent: object, width: int, height: int, path_game_over:str, path_wrong_answer: str, character: str, mainmenu_callback, choose_callback):
        super().__init__(parent=parent, width=width, height=height, path_game_over=path_game_over, path_wrong_answer=path_wrong_answer, character=character, main_menu_callback = mainmenu_callback, choose_callback=choose_callback)
        self.character = character
        self.mainmenu_callback = mainmenu_callback
        # Skill 1
        self.frame1 = skill_frame(self, 0.1)
        self.logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/allan/skills_icon/skill_1.png"), dark_image=Image.open("./assets/Characters/allan/skills_icon/skill_1.png"), size=(85, 85))
        self.lbl_skill_1 = CTkLabel(self.frame1, text="", image=self.logo_skill_1)
        self.lbl_skill_1.pack(padx=7, side="left")
        self.lbl_skill_1.bind("<Button-1>", lambda e: self.skill_1_notif(e))
        self.lbl_skill_1.bind("<Enter>", lambda e: self.on_hover_skill_1(e))
        self.lbl_skill_1.bind("<Leave>", lambda e: self.off_hover_skill_1(e))
        
        # Skill 2
        self.frame2 = skill_frame(self, 0.25)
        self.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/allan/skills_icon/skill_2.png"), dark_image=Image.open("./assets/Characters/allan/skills_icon/skill_2.png"), size=(85, 85))
        self.lbl_skill_2 = CTkLabel(self.frame2, text="", image=self.logo_skill_2)
        self.lbl_skill_2.pack(padx=7, side="left")
        self.lbl_skill_2.bind("<Button-1>", lambda e: self.skill_2(e))
        self.lbl_skill_2.bind("<Enter>", lambda e: self.on_hover_skill_2(e))
        self.lbl_skill_2.bind("<Leave>", lambda e: self.off_hover_skill_2(e))
        
        self.skill_1_name = "The Last Minute Man"
        
        # initialize that the skill 2 wasn't yet activated, this will be used under the keyboard module
        self.skill_2_active = False
        self.cooldown = False
        
    def on_hover_skill_1(self, event):
        self.hover_skill_1 = hover_frame(self, 400, 90, 1, self.character)
        
    def off_hover_skill_1(self, event):
        self.hover_skill_1.destroy()
        
    def on_hover_skill_2(self, event):
        self.hover_skill_2 = hover_frame(self, 400, 110, 2, self.character)
        
    def off_hover_skill_2(self, event):
        self.hover_skill_2.destroy()
        

        # passive skill
        # this method will be called under certain condition in the keyboard module
    def skill_1(self):
        # getting the correct key
        random_letter = random.choices(list(self.guess.correct_characters))[0].upper()
        
        # using the correct key to call the clicked() method 
        self.keyboard.clicked(self.keyboard.button_address[random_letter])
        
        # visually showing that the skill has been activated
        notice = CTkLabel(self, text=f"Passive Skill Activated: {self.skill_1_name}")
        notice.place(relx=0.5, rely=0.5, anchor="center")
        notice.after(2000, lambda: notice.destroy())
        
        # skill's sound effect
        play_audio.skill(self.character, "1")
        
    def skill_1_notif(self, event):
        # Just incase if the user is dumb enough to realize that passice skill doesn't need to be clicked
        notif = CTkLabel(self, text=f"This is a Passive skill")
        notif.place(relx=0.5, rely=0.5, anchor="center")
        notif.after(2000, lambda: notif.destroy())
        
    def skill_2(self, event):
        # setting up the cooldown or what level will the skill must be available again
        self.cooldown : int = self.guess.current_level + 2
        self.skill_2_active = True
        
        # disabled the skill button
        self.lbl_skill_2.unbind("<Button-1>")
        self.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/allan/skills_icon/skill_2_activate.png"), dark_image=Image.open("./assets/Characters/allan/skills_icon/skill_2_activate.png"), size=(85, 85))
        self.lbl_skill_2.configure(image=self.logo_skill_2)
        
        # to visually show that the skill is on cooldown
        self.lbl_skill_2.bind("<Button-1>", lambda e: self.skill_2_notif(e))
        
        # skill's sound effect
        play_audio.skill(self.character, "2")
    def skill_2_notif(self, event):
        notif = CTkLabel(self, text=f"This skill can be used again on Level {self.cooldown}")
        notif.place(relx=0.5, rely=0.5, anchor="center")
        notif.after(2000, lambda: notif.destroy())