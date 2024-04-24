from customtkinter import *

class Guess(CTkFrame):
    def __init__(self, parent: object, word_to_guess: str) -> None:
        super().__init__(master=parent, fg_color="transparent")
        self.parent = parent
        self.word_to_guess = word_to_guess
        self.frame_address = [] # list the will be used to store tuple combinations of
                                # letter and reference address to the frame widget
        
        for char in word_to_guess:
            lbl_frame = CTkFrame(self, 
                                 fg_color="#E6D439", 
                                 corner_radius=5, 
                                 height=38, 
                                 width=58)
            lbl_frame.pack(side="left", padx=5)
            self.frame_address.append((char, lbl_frame)) # appends a tuple
            
    def validate_char(self, char: str) -> bool:
        if char in self.word_to_guess:
            for tuple in self.frame_address:
                if char == tuple[0]: 
                    tuple[1].configure(fg_color="#2f1947")
                    lbl = CTkLabel(tuple[1], 
                                text=char, 
                                height=38, 
                                width=58,
                                font=("", -17.6, "bold"))
                    lbl.pack()
            
            return True
        return False
        
        