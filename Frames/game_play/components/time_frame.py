from customtkinter import *
from Frames.game_over import game_over
class Time(CTkFrame):
    def __init__ (self, parent, start_pos, end_pos, player_state: object, keyboard: object, character: str, character_object: object, mainmenu_callback, guess, choose_callback: object):
        super().__init__(master=parent, width=1000, height=80, corner_radius=0, border_width=5)
        self.player_state = player_state
        self.keyboard = keyboard
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.character = character
        self.character_object = character_object
        self.mainmenu_callback = mainmenu_callback
        self.choose_callback = choose_callback
        self.guess = guess
        self.active = True
        self.time_speed = 1000
        self.pack_propagate(False)
        self.place(relx=self.start_pos, rely=0.1, anchor="e")
        self.seconds = 200
        self.lbl_time = CTkLabel(self, text=str(self.seconds), font=("courier", -40, "bold"))
        self.lbl_time.pack(side="right", padx=20)
        
        self.animate()
        self.starting_time = 0
        self.starting_take_time()
        self.after(800, self.activate_time)
        
    def animate(self):
        if self.start_pos < self.end_pos:
            self.start_pos += 0.004
            self.place(relx=self.start_pos, rely=0.1, anchor="e")
            self.after(20, self.animate)
    
    # this is a recursion so if u want to stop the time, just change the self.active attribute
    def activate_time(self):
        if self.active:
            if self.seconds > 0:
                self.seconds -= 1
                self.lbl_time.configure(text=str(self.seconds))
                if self.character == "france":
            
                    if self.seconds == 0:
                        self.character_object.skill_1()
                
                self.after(self.time_speed, self.activate_time)
            else:
                self.player_state.GameOverAnimation()
                self.keyboard.disabled()
                game_over(self.keyboard.main_tk, self.keyboard.time_callback, self.keyboard, self.keyboard.points,  self.keyboard.character, self.guess, self.mainmenu_callback, self.choose_callback)
    def starting_take_time(self):
        self.starting_time = self.seconds

    def ending_take_time(self, storage, current_lvl):
        storage.append((self.starting_time - self.seconds) * current_lvl)
        if current_lvl == 20:
            storage.append(self.seconds*25)
            game_over(self.keyboard.main_tk, self.keyboard, self.keyboard.time_callback, self.keyboard.points,
                     self.keyboard.character, self.mainmenu_callback, self.guess)