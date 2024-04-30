from customtkinter import *

class SlideFrame(CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, width=1000, height=1000, corner_radius=0, border_width=5)
        
        self.start_pos = 1
        self.end_pos = 0.64
        self.pos = self.start_pos

        self.place(relx=0.05, rely=self.start_pos, anchor="n")
        self.pack_propagate(False)
        
        self.animate_upwards()
    def animate_upwards(self):
        if self.pos > self.end_pos:
            self.pos -= 0.013
            self.place(relx=0.5, rely=self.pos, anchor="n")
            self.after(10, self.animate_upwards)

    def frame_description(self, index: int):
        if index == 0:
            lbl = CTkLabel(self, text="just a normal dude", font=("", -50, "bold"))
            lbl.place(relx=0.5, rely=0.5, anchor="center")
