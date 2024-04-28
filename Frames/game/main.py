from customtkinter import CTkImage, CTkFrame, CTkLabel
from PIL import Image
from Frames.game.background import Player
from Frames.game.keyboard import Keyboard
from Frames.game.guess import Guess



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
    def __init__(self, parent: object, width: int, height: int, path_game_over:str, path_wrong_answer: str):
        super().__init__(master=parent, width=width, height=height, fg_color="transparent")
        
        parent_div = CTkFrame(self)
        parent_div.pack()

        default = Player(parent_div, path_game_over, path_wrong_answer, width, height)
        default.pack()
        
        frame = SlideFrame(parent_div, 1, 0.67)
        frame.pack_propagate(False)
        
        guess = Guess(frame)
        guess.pack(pady=20)

        keyboard = Keyboard(frame, guess, default, parent)
        keyboard.pack()
        