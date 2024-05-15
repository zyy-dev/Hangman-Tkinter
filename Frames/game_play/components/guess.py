from customtkinter import CTkFrame, CTkLabel, CTkImage
from Data.words import words
from PIL import Image

class Guess(CTkFrame):
    def __init__(self, parent: object, character_object: object, character: str) -> None:
        super().__init__(master=parent, fg_color="transparent")
        self.parent = parent
        self.character_object = character_object
        self.character = character
        self.current_level = 1
        self.category, self.word_to_guess = words.random_word(self.current_level)
        self.correct_characters = set(self.word_to_guess)
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
            self.correct_characters.remove(char)
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
    
    def reveal_answer(self):
        for letter, frame in self.frame_address:
            if letter in self.correct_characters:                
                frame.configure(fg_color="#3a002f")
                lbl = CTkLabel(frame, 
                            text=letter, 
                            height=38, 
                            width=58,
                            font=("", -17.6, "bold"))
                lbl.pack()
                
                    
    def next_level(self):
        self.current_level += 1
        if self.character == "renzo":
            if self.character_object.skill_1_state:
                self.current_level -= 1
                self.character_object.skill_1_state = False
        try:
            self.category, self.word_to_guess = words.random_word(self.current_level)
            self.correct_characters = set(self.word_to_guess)
            self.lbl_category.configure(text=self.category)
        except:
            pass
        
        self.frm.pack_forget()
        self.generate_boxes()
        
        if self.character == "richard":
            self.character_object.skill_2_remaining_time = 0
            try:
                if self.character_object.cooldown == self.current_level:
                    self.character_object.lbl_skill_2.unbind("<Button-1>")
                    
                    self.character_object.logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/richard/skills_icon/skill_2.jpeg"), dark_image=Image.open("./assets/Characters/richard/skills_icon/skill_2.jpeg"), size=(85, 85))
                    self.character_object.lbl_skill_2.configure(image=self.character_object.logo_skill_2)
                    self.character_object.lbl_skill_2.bind("<Button-1>", lambda e: self.character_object.skill_2_clicked(e))
                    self.character_object.skill_2_remaining_time = 20
            except:
                print ("skill 2 not used")
                

        
        
                    


        
        