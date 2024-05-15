from customtkinter import CTkFrame

class skill_frame(CTkFrame):
    def __init__ (self, parent: object, pos_y: int, start_pos_x = 1, end_pos_x = 0.928):
        super().__init__(master=parent, width=1000, height=100, corner_radius=0, border_width=5)
        self.start_pos_x = start_pos_x
        self.end_pos_x = end_pos_x
        self.pos_y = pos_y
        self.pack_propagate(False)
        
        self.place(relx=self.start_pos_x, rely=self.pos_y, anchor="w")
        self.animate()
        
    def animate(self):
        if self.start_pos_x > self.end_pos_x:
            self.start_pos_x -= 0.004
            self.place(relx=self.start_pos_x, rely=self.pos_y, anchor="w")
            self.after(20, self.animate)
            