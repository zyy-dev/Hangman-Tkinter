from customtkinter import *
from animation import Player


class HangMan(CTk):
    def __init__(self):
        super().__init__()
        # window settings
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()       
        self.geometry(f"{width}x{height}+-11+-5")
        self.minsize(width, height)
        set_appearance_mode("dark")
        self.title("Hangman")

        # assemble
        default = Player(self, "./assets/Animation_Main Menu", "./assets/Animation_Wrong Answer/default_player", width, height, 10)
        default.GameOverAnimation()
        default.pack()

app = HangMan()
app.mainloop()