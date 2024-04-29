from customtkinter import CTkFrame
from Frames.game.components.player_state import Player
from Frames.game.components.keyboard import Keyboard
from Frames.game.components.guess import Guess
from Frames.game.components.time_frame import Time


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
            

class default_character(CTkFrame):
    def __init__(self, parent: object, width: int, height: int, path_game_over:str, path_wrong_answer: str, character: str):
        super().__init__(master=parent, width=width, height=height, fg_color="transparent")
        
        parent_div = CTkFrame(self)
        parent_div.pack()

        player_state = Player(parent_div, path_game_over, path_wrong_answer, width, height, self.stop_time)
        player_state.pack()
      
        frame = SlideFrame(parent_div, 1, 0.64)

        self.guess = Guess(frame)
        self.guess.pack(pady=20)

        self.keyboard = Keyboard(frame, self.guess, player_state, parent, character, self)
        self.keyboard.pack()
        
        self.time = Time(parent_div, 0, 0.08, player_state, self.keyboard)
        
    def stop_time(self):
        self.time.active = False