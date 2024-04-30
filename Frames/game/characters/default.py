from customtkinter import CTkFrame, CTkLabel
from Frames.game.components.player_state import Player
from Frames.game.components.keyboard import Keyboard
from Frames.game.components.guess import Guess
from Frames.game.components.time_frame import Time


class SlideFrame(CTkFrame):
    def __init__(self, parent, start_pos, end_pos, width):
        super().__init__(master=parent, width=width, height=1000, corner_radius=0, border_width=5)
        
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.pos = self.start_pos
        self.anchor = "n" if self.start_pos == 1 else "s"

        self.place(relx=0.05, rely=self.start_pos, anchor=self.anchor)
        self.pack_propagate(False)
        
        if self.anchor == "n":
            self.animate_upwards()
        else:
            self.animate_downwards()

    def animate_upwards(self):
        if self.pos > self.end_pos:
            self.pos -= 0.013
            self.place(relx=0.5, rely=self.pos, anchor=self.anchor)
            self.after(10, self.animate_upwards)

    def animate_downwards(self):
        if self.pos < self.end_pos:
            self.pos += 0.004
            self.place(relx=0.5, rely=self.pos, anchor=self.anchor)
            self.after(20, self.animate_downwards)
            

class default_character(CTkFrame):
    def __init__(self, parent: object, width: int, height: int, path_game_over:str, path_wrong_answer: str, character: str):
        super().__init__(master=parent, width=width, height=height, fg_color="transparent")
        
        parent_div = CTkFrame(self)
        parent_div.pack()

        player_state = Player(parent_div, path_game_over, path_wrong_answer, width, height, self)
        player_state.pack()
      
        frame = SlideFrame(parent_div, 1, 0.64, 1000)

        self.guess = Guess(frame, self, character)
        self.guess.pack(pady=20)

        self.keyboard = Keyboard(frame, self.guess, player_state, parent, character, self)
        self.keyboard.pack()
        
        self.time = Time(parent_div, 0, 0.07, player_state, self.keyboard, character, self)
        
        frm_lvl = SlideFrame(parent_div, 0, 0.05, 200)
        self.lbl_lvl = CTkLabel(frm_lvl, text=f"Level: {self.guess.current_level}", font=("courier", -20, "bold"))
        self.lbl_lvl.pack(side="bottom", pady=7)