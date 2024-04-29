import customtkinter as ctk
from PIL import Image
import os

class Player(ctk.CTkLabel):
    def __init__(self, parent: object, folder_path_gameover :str, folder_path_mistake: str, width: int, height: int, stop_time_callback: object, delay = 11) -> None:
        super().__init__(master = parent, text="")
        self.folder_path_gameover = folder_path_gameover
        self.folder_path_mistake = folder_path_mistake
        self.width = width
        self.height = height
        self.parent = parent
        self.delay = delay
        self.stop_time = stop_time_callback
        self.import_images()
        
        self.WrongAnswer(0)
        
    def import_images(self) -> list[str]:
        image_paths = []
        for file_name in os.listdir(self.folder_path_gameover):
            image_paths.append(self.folder_path_gameover + "/" + file_name)
        self.images_path_gameover = sorted(image_paths, key= lambda item: int(item.split("/")[-1][:-4]))
        
        image_paths = [] 
        for file_name in os.listdir(self.folder_path_mistake):
            image_paths.append(self.folder_path_mistake + "/" + file_name)
        self.images_path_mistake = sorted(image_paths, key= lambda i: int(i.split("/")[-1][:-4]))
    
    def WrongAnswer(self, mistakes: int):
        image = ctk.CTkImage(light_image=Image.open(self.images_path_mistake[mistakes]), dark_image=Image.open(self.images_path_mistake[mistakes]), size=(self.width,self.height))
        self.configure(image=image)
    
    def GameOverAnimation(self, i=0):
        if i == 0: 
            self.stop_time()
        if i < len(self.images_path_gameover):
            image = ctk.CTkImage(light_image=Image.open(self.images_path_gameover[i]), dark_image=Image.open(self.images_path_gameover[i]), size=(self.width,self.height))
            self.configure(image=image)
            self.after(self.delay, lambda i=i+1: self.GameOverAnimation(i))
        



