from customtkinter import *
from pages.game.animation import Player
from pages.game.keyboard import Keyboard
from pages.game.guess import Guess


class HangMan(CTkFrame):
    def __init__(self, parent: object, width: int, height: int, main_tk: object):
        super().__init__(master=parent, fg_color="transparent", width=width, height=height)
        self.parent = parent

        # assemble
        default = Player(self, "./assets/Animation_Game Over/default_player", "./assets/Animation_Wrong Answer/default_player")
        default.place(rely=0.05, relx=0.5, anchor="n")

        guess = Guess(self)
        guess.place(rely=0.65, relx=0.5, anchor="n")

        keyboard = Keyboard(self, guess, default, main_tk)
        keyboard.place(rely=0.8, relx=0.5, anchor="n")