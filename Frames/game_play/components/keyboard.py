from customtkinter import *
from PIL import Image
from Frames.game_play.components.audio import play_audio
from Frames.game_over import game_over
class Keyboard(CTkFrame):
    def __init__ (self, parent: object, guess: object, player_state: object, main_tk: object, character: str, character_object: object, time_callback, main_menu_callback, choose_callback) -> None:
        super().__init__(master=parent, fg_color="transparent")
        self.parent = parent
        self.guess = guess
        self.player_state = player_state
        self.main_tk = main_tk
        self.character = character
        self.character_object = character_object
        self.main_menu_callback = main_menu_callback
        self.choose_callback = choose_callback
        self.mistakes = 0
        self.correct = 0
        self.button_address = {}
                            # key: character
                            # value: reference address of Button Widgets
        self.key_already_pressed = []
        self.points = []
        self.time_callback = time_callback
        
        Upper_Button_Frame = CTkFrame(self, fg_color="transparent")
        Upper_Button_Frame.pack(pady=8)
        for char in "ABCDEFGHIJKLMN":
            btn = CTkButton(Upper_Button_Frame, 
                            text=char, 
                            width=45,
                            height=30, 
                            fg_color="#520CA1", 
                            corner_radius=5, 
                            text_color="#FFFFFF", 
                            font=("", -16, "bold"))
            
            btn.pack(side="left", padx=8)
            btn.bind("<Enter>", lambda event, btn=btn: self.on_hover(btn, event))
            btn.bind("<Leave>", lambda event, btn=btn: self.off_hover(btn, event)) 
            btn.configure(command=lambda btn=btn: self.clicked(btn))
            self.button_address[char] = btn
        

        Lower_Button_Frame = CTkFrame(self, fg_color="transparent")
        Lower_Button_Frame.pack(pady=8)
        for char in "OPQRSTUVWXYZ":
            btn = CTkButton(Lower_Button_Frame, 
                            text=char, 
                            width=45,
                            height=30, 
                            fg_color="#520CA1", 
                            corner_radius=5, 
                            text_color="#FFFFFF", 
                            font=("Arial", -16, "bold"))
            
            btn.pack(side="left", padx=8)
            btn.bind("<Enter>", lambda event, btn=btn: self.on_hover(btn, event))
            btn.bind("<Leave>", lambda event, btn=btn: self.off_hover(btn, event)) 
            btn.configure(command=lambda btn=btn: self.clicked(btn))
            self.button_address[char] = btn
            
            # Using default arguments in lambda functions is a way to capture the value of a variable at the time the lambda function is defined.
        
        self.main_tk.bind("<Key>", self.key_pressed)
        
    def on_hover(self, btn: object, event) -> None:
        btn.configure(text_color="#350a66", fg_color="#e757bc")
        
    def off_hover(self, btn: object, event) -> None:
        btn.configure(text_color="#FFFFFF", fg_color="#520CA1")
        
    def clicked(self, btn: object) -> None:
        # visual changes and unbinding
        char = btn.cget("text")
        btn.unbind("<Enter>")
        btn.unbind("<Leave>")
        btn.configure(state="disabled")
        btn.configure(fg_color="#2f1947")
        btn.configure(text_color="#7A7381")
        self.key_already_pressed.append(char)

        # if wrong key
        if not self.guess.validate_char(char):
            # visual changes
            btn.configure(border_width=1)
            btn.configure(border_color="red")
            
            
            # skill related 
            if self.character == "allan":
                if self.mistakes == 4:
                    self.character_object.skill_1()
                    
                # this will make the wrong key to dont reflect with the counts of mistake    
                if self.character_object.skill_2_active:
                    # re-declare it because we only want the skill to take effect once
                    self.character_object.skill_2_active = False
                    
                    self.character_object.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/allan/skills_icon/skill_2.png"), dark_image=Image.open("./assets/Characters/allan/skills_icon/skill_2.png"), size=(85, 85))
                    self.character_object.lbl_skill_2.configure(image=self.character_object.logo_skill_2 )
                    
                    # stop the method before it reflect the increment to self.mistakes
                    return 
                
            if self.character == "france":
                if self.character_object.skill_2_state:
                    # stop the method before it reflect the increment to self.mistakes
                    return
                
            if self.character == "zyrus":
                if self.character_object.skill_1_state:
                    # stop the method before it reflect the increment to self.mistakes
                    return
                    
            
            self.mistakes += 1
                
            # if game over
            if self.mistakes > 5:
                btn.configure(state="disabled")
                self.player_state.GameOverAnimation()
                self.guess.reveal_answer()
                self.disabled()
                self.after(2000, lambda: game_over(self.main_tk, self, self.time_callback, self.points, self.character, self.guess, self.main_menu_callback, self.choose_callback))
            else:
                # if wrong
                play_audio.wrong()
                self.player_state.WrongAnswer(self.mistakes)
        # if correct
        else:
            play_audio.correct()
            self.correct += 1
            if self.correct == len(set(self.guess.word_to_guess)):
                play_audio.win()
                self.time_callback.ending_take_time(self.points, self.guess.current_level)
                self.disabled()
                
                if self.character == "zyrus":
                    if self.character_object.skill_2_state:
                        self.points.pop()
                        
                if self.character == "renzo":
                    if self.character_object.skill_2_state:
                        self.points[-1] /= 2
                        
                self.after(800, self.reset) 
        
    # for key binding or using the physical keyboard
    def key_pressed(self, event) -> None:
        selected = event.char.upper()
        if selected in self.button_address and selected not in self.key_already_pressed:
            self.clicked(self.button_address[selected])
            
            
    def disabled(self) -> None:
        print ("disabeld all")
        self.main_tk.unbind("<Key>")
        for char in self.button_address:
            self.button_address[char].configure(state="disabled")
            self.button_address[char].unbind("<Enter>")
            self.button_address[char].unbind("<Leave>")
    
    # this means proceed to next level
    def reset(self) -> None:
        self.time_callback.starting_take_time()
        self.player_state.WrongAnswer(0)
        self.guess.next_level()
        self.main_tk.bind("<Key>", self.key_pressed)
        self.finished = "Game Finished!"
        self.character_object.lbl_lvl.configure(text=f"Level: {self.guess.current_level if self.guess.current_level < 21 else self.finished}")
        self.mistakes = 0
        self.correct = 0
        self.key_already_pressed = []
        for char in self.button_address:                       
            self.button_address[char].configure(state="normal", fg_color="#520CA1", text_color="#FFFFFF", border_width=0)
            self.button_address[char].bind("<Enter>", lambda event, btn=self.button_address[char]: self.on_hover(btn, event))
            self.button_address[char].bind("<Leave>", lambda event, btn=self.button_address[char]: self.off_hover(btn, event))
        
        # skill related        
        if self.character == "allan":
            if self.character_object.cooldown == self.guess.current_level:
                # unbind to the notification
                self.character_object.lbl_skill_2.unbind("<Button-1>")
                self.character_object.lbl_skill_2.bind("<Button-1>", self.character_object.skill_2)
                self.character_object.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/allan/skills_icon/skill_2.png"), dark_image=Image.open("./assets/Characters/allan/skills_icon/skill_2.png"), size=(85, 85))
                self.character_object.lbl_skill_2.configure(image=self.character_object.logo_skill_2)

                    
        if self.character == "zyrus":
            if self.character_object.cooldown == self.guess.current_level:
                # unbind to the notification
                self.character_object.lbl_skill_1.unbind("<Button-1>")
                
                # bind again
                self.character_object.lbl_skill_1.bind("<Button-1>", self.character_object.skill_1)
                self.character_object.logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/zyrus/skills_icon/skill_1.jpg"), dark_image=Image.open("./assets/Characters/zyrus/skills_icon/skill_1.jpg"), size=(85, 85))
                self.character_object.lbl_skill_1.configure(image=self.character_object.logo_skill_1)

        if self.character == "renzo":
            if self.character_object.cooldown2 == self.guess.current_level:
                
                # unbind to the notification
                self.character_object.lbl_skill_2.unbind("<Button-1>")
                
                # bind again
                self.character_object.lbl_skill_2.bind("<Button-1>", self.character_object.skill_2)
                self.character_object.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/renzo/skills_icon/skill_2.jpg"), dark_image=Image.open("./assets/Characters/renzo/skills_icon/skill_2.jpg"), size=(85, 85))
                self.character_object.lbl_skill_2.configure(image=self.character_object.logo_skill_2)
                
                
            if self.character_object.cooldown1 == self.guess.current_level:
                
                # unbind to the notification
                self.character_object.lbl_skill_1.unbind("<Button-1>")
                
                # bind again
                self.character_object.lbl_skill_1.bind("<Button-1>", self.character_object.skill_1)
                self.character_object.logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/renzo/skills_icon/skill_1.jpg"), dark_image=Image.open("./assets/Characters/renzo/skills_icon/skill_1.jpg"), size=(85, 85))
                self.character_object.lbl_skill_1.configure(image=self.character_object.logo_skill_1)