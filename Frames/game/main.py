from customtkinter import CTkFrame
from Frames.game.player import Player
from Frames.game.keyboard import Keyboard
from Frames.game.guess import Guess
from Frames.game.time_frame import Time


class SlideFrame(CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent, width=1000, height=1000, corner_radius=0, border_width=5)
        
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.pos = self.start_pos

        self.place(relx=0.05, rely=self.start_pos, anchor="n")
        self.pack_propagate(False)
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

        player_state = Player(parent_div, path_game_over, path_wrong_answer, width, height, self.stop_time)
        player_state.pack()
        
        
        
        frame = SlideFrame(parent_div, 1, 0.64)

        guess = Guess(frame)
        guess.pack(pady=20)

        keyboard = Keyboard(frame, guess, player_state, parent)
        keyboard.pack()
        
        self.time = Time(parent_div, 0, 0.08, player_state, keyboard)
        
    def stop_time(self):
        self.time.active = False
        