from customtkinter import *
from words import Words

class Guess(CTkFrame):
    def __init__(self, parent: object, word_to_guess: str) -> None:
        super().__init__(master=parent, fg_color="transparent")
        self.parent = parent
        self.word_to_guess = word_to_guess
        
        for char in word_to_guess:
            lbl = CTkLabel(self, 
                           text="_",
                           font=("", -50, "bold"))
            lbl.pack(side="left", padx=5)
            
    def validate_char(self, char: str) -> bool:
        print ("uy gumana")
        if char in self.word_to_guess:
            return True
        return False
            
            
if __name__ == "__main__":
    root = CTk()
    root.geometry("500x500")
    word = Words()
    guess = Guess(root, word.lvl_1())
    guess.pack()
    root.mainloop()
        
        