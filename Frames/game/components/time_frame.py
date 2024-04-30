from customtkinter import *

class Time(CTkFrame):
    def __init__ (self, parent, start_pos, end_pos, player_state: object, keyboard: object, character: str, character_object: object):
        super().__init__(master=parent, width=1000, height=80, corner_radius=0, border_width=5)
        self.player_state = player_state
        self.keyboard = keyboard
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.character = character
        self.character_object = character_object
        
        self.active = True
        self.time_speed = 1000
        self.pack_propagate(False)
        self.place(relx=self.start_pos, rely=0.1, anchor="e")
        self.seconds = 200
        self.lbl_time = CTkLabel(self, text=str(self.seconds), font=("courier", -40, "bold"))
        self.lbl_time.pack(side="right", padx=20)
        
        self.animate()
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
                