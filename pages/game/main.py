from customtkinter import CTkImage, CTkFrame, CTkLabel
from PIL import Image
from pages.game.background import Player
from pages.game.keyboard import Keyboard
from pages.game.guess import Guess



class SlideFrame(CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent, width=1000, height=1000, corner_radius=0, fg_color="transparent", border_width=5)
        
        self.start_pos = start_pos + 0.04
        self.end_pos = end_pos - 0.03

        self.pos = self.start_pos

        self.place(relx=0.05, rely=self.start_pos, anchor="n")
        self.animate()

    def animate(self):
        if self.pos > self.end_pos:
            self.pos -= 0.006
            self.place(relx=0.5, rely=self.pos, anchor="n")
            self.after(10, self.animate)



class HangMan(CTkFrame):
    def __init__(self, parent: object, width: int, height: int, main_tk: object):
        super().__init__(master=parent, width=width, height=height, fg_color="transparent")
        
        parent_div = CTkFrame(self)
        parent_div.pack()

        default = Player(parent_div, "./assets/Animation_Game Over/default_player", "./assets/Animation_Wrong Answer/default_player", width, height)
        default.pack()
        
        frame = SlideFrame(parent_div, 1, 0.67)
        frame.pack_propagate(False)
        
        guess = Guess(frame)
        guess.pack(pady=20)

        keyboard = Keyboard(frame, guess, default, main_tk)
        keyboard.pack()
        