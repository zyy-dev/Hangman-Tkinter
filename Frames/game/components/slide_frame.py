from customtkinter import CTkFrame

class slide_frame(CTkFrame):
    def __init__(self, parent, start_pos, end_pos, width):
        super().__init__(master=parent, width=width, height=1000, corner_radius=0, border_width=5)
        
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.pos = self.start_pos
        self.anchor = "n" if self.start_pos == 1 else "s"

        self.place(relx=0.5, rely=self.start_pos, anchor=self.anchor)
        self.pack_propagate(False)

    def animate_upwards(self):
        if self.pos > self.end_pos:
            self.pos -= 0.013
            self.place(relx=0.5, rely=self.pos, anchor=self.anchor)
            self.after(10, self.animate_upwards)

    def animate_downwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.016
            self.place(relx=0.5, rely=self.pos, anchor=self.anchor)
            self.after(10, self.animate_downwards)