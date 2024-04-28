from customtkinter import *
from PIL import Image
from Frames.game.main import HangMan

class Choices(CTkFrame):
    def __init__(self, parent: object, width:int, height: int):
        super().__init__(master=parent, width=width, height=height)
        self.parent = parent
        self.width = width
        self.height = height
        self.image_paths = ["./assets/Characters/default.png",
                            "./assets/Characters/allan.png",
                            "./assets/Characters/renzo.png",
                            "./assets/Characters/france.png",
                            "./assets/Characters/richard.png",
                            "./assets/Characters/zyrus.png"]
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
        if self.index == len(self.image_paths) - 1:
            self.index -= 1
        else:
            self.index += 1
        self.lbl.configure(image=self.image_paths[self.index])
    
    def left(self):
        if self.index == 0:
            self.index = len(self.image_paths) - 1
        else:
            self.index -= 1
        self.lbl.configure(image=self.image_paths[self.index])
    
    def play(self):
        if self.index == 0:
            default = HangMan(self.parent, self.width, self.height, "./assets/Animation_Game Over/default", "./assets/Animation_Wrong Answer/default")
            default.pack()
            self.pack_forget()
        if self.index == 1:
            return "allan"
        if self.index == 2:
            return "renzo"
        if self.index == 3:
            return "france"
        if self.index == 4:
            return "richard"
        if self.index == 5:
            return "zyrus"