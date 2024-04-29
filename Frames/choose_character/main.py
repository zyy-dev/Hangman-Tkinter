from customtkinter import *
from PIL import Image
from Frames.game.characters.default import default_character
from Frames.game.characters.allan import allan_character
from Frames.game.characters.zyrus import zyrus_character
from Frames.game.characters.richard import richard_character
from Frames.game.characters.renzo import renzo_character
from Frames.game.characters.france import france_character

class Choices(CTkFrame):
    def __init__(self, parent: object, width:int, height: int):
        super().__init__(master=parent, width=width, height=height)
        self.parent = parent
        self.width = width
        self.height = height
        self.image_paths = ["assets/Characters/default/default.png",
                            "assets/Characters/allan/allan.png",
                            "assets/Characters/renzo/renzo.png",
                            "assets/Characters/france/france.png",
                            "assets/Characters/richard/richard.png",
                            "assets/Characters/zyrus/zyrus.png"]
        self.index = 0
        
        self.image = CTkImage(light_image=Image.open(self.image_paths[self.index]), dark_image=Image.open(self.image_paths[self.index]), size=(self.width, self.height))
        self.lbl = CTkLabel(self, text="", image=self.image)
        self.lbl.pack()
        
        self.btn_right = CTkButton(self, text=">", command=self.right)
        self.btn_right.place(relx=0.8, rely=0.5, anchor="center")
        
        self.btn_right = CTkButton(self, text="<", command=self.left)
        self.btn_right.place(relx=0.2, rely=0.5, anchor="center")
        
        self.btn_play = CTkButton(self, text="play", command=self.play)
        self.btn_play.place(relx=0.5, rely=0.8, anchor="center")
        
    def right(self):
        print ("right ffdsagesgetgwWRGwegrsgrsgwetgweggsdfsdf")
        if self.index == len(self.image_paths) - 1:
            self.index = 0
        else:
            self.index += 1
        self.image = CTkImage(light_image=Image.open(self.image_paths[self.index]), dark_image=Image.open(self.image_paths[self.index]), size=(self.width, self.height))
        self.lbl.configure(image=self.image)
    
    def left(self):
        if self.index == 0:
            self.index = len(self.image_paths) - 1
        else:
            self.index -= 1
        self.image = CTkImage(light_image=Image.open(self.image_paths[self.index]), dark_image=Image.open(self.image_paths[self.index]), size=(self.width, self.height))
        self.lbl.configure(image=self.image)
    
    def play(self):
        if self.index == 0:
            default = default_character(self.parent, self.width, self.height, "./assets/Characters/default/game_over", "./assets/Characters/default/wrong_answer", "default")
            default.pack()
            self.pack_forget()
        if self.index == 1:
            self.pack_forget()
            allan = allan_character(self.parent, self.width, self.height, "./assets/Characters/allan/game_over", "./assets/Characters/allan/wrong_answer", "allan")
            allan.pack()
        if self.index == 2:
            renzo = renzo_character(self.parent, self.width, self.height, "./assets/Characters/renzo/game_over", "./assets/Characters/renzo/wrong_answer", "renzo")
            renzo.pack()
            self.pack_forget()
        if self.index == 3:
            france = france_character(self.parent, self.width, self.height, "./assets/Characters/france/game_over", "./assets/Characters/france/wrong_answer", "france")
            france.pack()
            self.pack_forget()
        if self.index == 4:
            richard = richard_character(self.parent, self.width, self.height, "./assets/Characters/richard/game_over", "./assets/Characters/richard/wrong_answer", "richard")
            richard.pack()
            self.pack_forget()
        if self.index == 5:
            zyrus = zyrus_character(self.parent, self.width, self.height, "./assets/Characters/zyrus/game_over", "./assets/Characters/zyrus/wrong_answer")
            zyrus.pack()
            self.pack_forget()