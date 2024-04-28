from customtkinter import *
from Frames.game.components.words import words

class Guess(CTkFrame):
    def __init__(self, parent: object) -> None:
        super().__init__(master=parent, fg_color="transparent")
        self.parent = parent
        self.current_level = 1
        self.category, self.word_to_guess = words.random_word(self.current_level)
        self.frame_address = [] # list the will be used to store tuple combinations of
                                # letter and reference address to the frame widget
                                
                                
        self.lbl_category = CTkLabel(self, text=self.category, font=("", -17, "bold"))
        self.lbl_category.pack(pady=(0, 20))
        self.generate_boxes()
    def generate_boxes(self):
        self.frm = CTkFrame(self, fg_color="transparent")
        self.frm.pack()
        for char in self.word_to_guess:
            lbl_frame = CTkFrame(self.frm, 
                                 fg_color="#E6D439", 
                                 corner_radius=5, 
                                 height=38, 
                                 width=58)
            lbl_frame.pack(side="left", padx=5)
            self.frame_address.append((char, lbl_frame)) # appends a tuple
            
    def validate_char(self, char: str) -> bool:
        
        if char in self.word_to_guess:
            for letter, frame in self.frame_address:
                if char == letter:
                    frame.configure(fg_color="#2f1947")
                    lbl = CTkLabel(frame, 
                                text=char, 
                                height=38, 
                                width=58,
                                font=("", -17.6, "bold"))
                    lbl.pack()
            return True
        return False
                    
    def next_level(self):
        self.current_level += 1
        self.category, self.word_to_guess = words.random_word(self.current_level)
        self.lbl_category.configure(text=self.category)
        self.frm.pack_forget()
        self.generate_boxes()
            
        
        
                    


        
        