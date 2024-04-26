from customtkinter import CTkImage, CTkFrame, CTkLabel
from PIL import Image
from pages.game.player_state import Player
from pages.game.keyboard import Keyboard
from pages.game.guess import Guess


class HangMan(CTkFrame):
    def __init__(self, parent: object, width: int, height: int, main_tk: object):
        super().__init__(master=parent, width=width, height=height, fg_color="transparent")
        
        
        background_image = CTkImage(light_image=Image.open("pages/game/20.png"), dark_image=Image.open("pages/game/20.png"), size=(width, height))
        background = CTkLabel(self, text="", image=background_image)
        
        background.pack()

        default = Player(background, "./assets/Animation_Game Over/default_player", "./assets/Animation_Wrong Answer/default_player")
        default.place(rely=0.05, relx=0.5, anchor="n")

        guess = Guess(background)
        guess.place(rely=0.65, relx=0.5, anchor="n")

        keyboard = Keyboard(background, guess, default, main_tk)
        keyboard.place(rely=0.8, relx=0.5, anchor="n")
        