import customtkinter as ctk
from PIL import Image
import os

class Player:
    def __init__(self, parent: object, folder_path :str, delay: int) -> int:
        self.folder_path = folder_path
        self.frames = self.import_images()
        print (self.frames)
        self.parent = parent
        self.image_label = ctk.CTkLabel(parent, text="")
        self.image_label.pack()
        self.delay = delay
        
        
    def import_images(self):
        image_paths = []
        for file_name in os.listdir(self.folder_path):
            image_paths.append(self.folder_path + "/" + file_name)
        
        return sorted(image_paths, key= lambda i: int(i.split("/")[4][:-4]))
    
    def GameOverAnimation(self, i = 0):
        if i == len(self.frames):
            return
        image = ctk.CTkImage(light_image=Image.open(self.frames[i]), dark_image=Image.open(self.frames[i]), size=(640,360))
        self.image_label.configure(image=image)
        self.image_label.image = image
        self.parent.after(self.delay, lambda: self.GameOverAnimation((i + 1)))

if __name__ == "__main__":
    root = ctk.CTk()
    zyy = Player(root, "./assets/Animation_Game Over/default_player", 10)
    zyy.GameOverAnimation()
    
    
    root.mainloop()
