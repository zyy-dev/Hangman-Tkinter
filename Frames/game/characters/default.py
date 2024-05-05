from customtkinter import CTkFrame, CTkLabel
from Frames.game.components.player_state import Player
from Frames.game.components.keyboard import Keyboard
from Frames.game.components.guess import Guess
from Frames.game.components.time_frame import Time
from Frames.game.components.slide_frame import slide_frame  

class default_character(CTkFrame):
    def __init__(self, parent: object, width: int, height: int, path_game_over:str, path_wrong_answer: str, character: str):
        super().__init__(master=parent, width=width, height=height, fg_color="transparent")

        # placement of the background image or the character
        player_state = Player(self, path_game_over, path_wrong_answer, width, height, self)
        player_state.pack()
        
        # sub frame for keyboard and guess modules
        frame = slide_frame(self, 1, 0.64, 1000)
        frame.animate_upwards()

        self.guess = Guess(frame, self, character)
        self.guess.pack(pady=20)

        self.keyboard = Keyboard(frame, self.guess, player_state, parent, character, self, self.time_callback)
        self.keyboard.pack()
        
        self.time = Time(self, 0, 0.08, player_state, self.keyboard, character, self)
        self.time_callback()
        
        frm_lvl = slide_frame(self, 0.05, 0, 200)
        self.lbl_lvl = CTkLabel(frm_lvl, text=f"Level: {self.guess.current_level}", font=("courier", -20, "bold"))
        self.lbl_lvl.pack(side="bottom", pady=7)
        
    def time_callback(self):
        self.keyboard.time_callback = self.time