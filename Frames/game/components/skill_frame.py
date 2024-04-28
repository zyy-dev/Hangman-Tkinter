from customtkinter import *

class Time(CTkFrame):
    def __init__ (self, parent, start_pos, end_pos):
        super().__init__(master=parent, width=1000, height=100, corner_radius=0, border_width=5)
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.pack_propagate(False)
        
        self.place(relx=self.start_pos, rely=0.7, anchor="w")
        self.animate()
        
    def animate(self):
        if self.start_pos > self.end_pos:
            self.start_pos -= 0.006
            self.place(relx=self.start_pos, rely=0.1, anchor="w")
            self.after(10, self.animate)
            