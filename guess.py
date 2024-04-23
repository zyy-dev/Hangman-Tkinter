from customtkinter import *
from words import Words

class Guess(CTkFrame):
    def __init__(self, parent: object, word_to_guess: str) -> None:
        super().__init__(master=parent, fg_color="transparent")
        self.parent = parent
        self.word_to_guess = word_to_guess
        self.frame_address = {}
                        # key: character
                        # value: reference address of Frame Widgets
        for char in word_to_guess:
            lbl_frame = CTkFrame(self, 
                                 fg_color="#E6D439", 
                                 corner_radius=5, 
                                 height=38, 
                                 width=58)
            lbl_frame.pack(side="left", padx=5)
            self.frame_address[char] = lbl_frame
            
    def validate_char(self, char: str) -> bool:
        mistakes = 0
        if char in self.word_to_guess:
            self.frame_address[char].configure(fg_color="#2f1947")
            lbl = CTkLabel(self.frame_address[char], 
                           text=char, 
                           height=38, 
                           width=58,
                           font=("", -17.6, "bold"))
            lbl.pack()
            mistakes += 1
            if mistakes > 6:
                return "Game Over"
            return True
        return False
            
if __name__ == "__main__":
    root = CTk()
    root.geometry("500x500")
    word = Words()
    guess = Guess(root, word.lvl_1())
    guess.pack()
    root.mainloop()
        
        