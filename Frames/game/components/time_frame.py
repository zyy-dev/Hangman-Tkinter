from customtkinter import *

class Time(CTkFrame):
    def __init__ (self, parent, start_pos, end_pos, player_state: object, keyboard: object):
        super().__init__(master=parent, width=1000, height=80, corner_radius=0, border_width=5)
        self.player_state = player_state
        self.keyboard = keyboard
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.active = True
        self.time_speed = 1000
        self.pack_propagate(False)
        self.place(relx=self.start_pos, rely=0.1, anchor="e")
        self.seconds = 100
        self.lbl_time = CTkLabel(self, text=str(self.seconds), font=("courier", -40, "bold"))
        self.lbl_time.pack(side="right", padx=20)
        
        self.animate()
        self.after(800, self.activate_time)
        
    def animate(self):
        if self.start_pos < self.end_pos:
            self.start_pos += 0.006
            self.place(relx=self.start_pos, rely=0.1, anchor="e")
            self.after(10, self.animate)
            
    def activate_time(self):
        if self.seconds > 0 and self.active:
            self.seconds -= 1
            self.lbl_time.configure(text=str(self.seconds))
            self.after(self.time_speed, self.activate_time)
        else:
            self.player_state.GameOverAnimation()
            self.keyboard.disabled()