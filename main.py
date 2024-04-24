from customtkinter import *
from animation import Player
from keyboard import Keyboard
from guess import Guess


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
        default = Player(self, "./assets/Animation_Game Over/default_player", "./assets/Animation_Wrong Answer/default_player")
        default.place(rely=0.05, relx=0.5, anchor="n")

        guess = Guess(self)
        guess.place(rely=0.65, relx=0.5, anchor="n")

        keyboard = Keyboard(self, guess, default) #connects the guess and animation module to keyboard
        keyboard.place(rely=0.8, relx=0.5, anchor="n")

app = HangMan()
app.mainloop()


