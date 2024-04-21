import customtkinter as ctk
from PIL import Image
import os

class Player(ctk.CTkLabel):
    def __init__(self, folder_path_gameover :str, folder_path_mistake: str, delay: int, parent = None) -> None:
        super().__init__(master = parent, text="")
        self.folder_path_gameover = folder_path_gameover
        self.folder_path_mistake = folder_path_mistake
        self.parent = parent
        self.delay = delay
        self.frames = self.import_images()
        
    def set_parent(self, parent):
        self.parent = parent
        
    def import_images(self) -> list[str]:
        image_paths = []
        for file_name in os.listdir(self.folder_path_gameover):
            image_paths.append(self.folder_path_gameover + "/" + file_name)
        return sorted(image_paths, key= lambda i: int(i.split("/")[4][:-4]))
    
    def GameOverAnimation(self, i = 0):
        if i == len(self.frames):
            return
        image = ctk.CTkImage(light_image=Image.open(self.frames[i]), dark_image=Image.open(self.frames[i]), size=(640,360))
        self.configure(image=image)
        self.parent.after(self.delay, lambda: self.GameOverAnimation((i + 1)))
        
    def WrongAnswer(self, mistakes: int):
        image_paths = []
        for file_name in os.listdir(self.folder_path_mistake):
            image_paths.append(self.folder_path_mistake + "/" + file_name)
        image_paths = sorted(image_paths, key= lambda i: int(i.split("/")[4][:-4]))

        image = ctk.CTkImage(light_image=Image.open(image_paths[mistakes]), dark_image=Image.open(image_paths[mistakes]), size=(640,360))
        self.configure(image=image)
    
default = Player("./assets/Animation_Game Over/default_player", "./assets/Animation_Wrong Answer/default_player", 10)


