from customtkinter import *
from animation import Animation

class MainMenu(CTkFrame):
    def __init__(self, parent: object, width: int, height: int, start_game_callback):
        super().__init__(master=parent, width=width, height=height)
        self.parent = parent
        self.width = width
        self.height = height

        default = Animation(self, "./assets/Animation_Open App", self.width, self.height)
        default.pack()
        
        self.btn = CTkButton(self, text="Start Game", font=("", -30, "bold"), corner_radius=0, command=start_game_callback)
        self.btn.place(relx=0.5, rely=0.5, anchor="center")

