import customtkinter as ctk
from PIL import Image
import os

class Player(ctk.CTkLabel):
    def __init__(self, parent: object, folder_path :str, delay: int) -> int:
        super().__init__(master = parent, text="")
        self.folder_path = folder_path
        self.parent = parent
        self.delay = delay
        self.frames = self.import_images()
        
    def import_images(self):
        image_paths = []
        for file_name in os.listdir(self.folder_path):
            image_paths.append(self.folder_path + "/" + file_name)
        return sorted(image_paths, key= lambda i: int(i.split("/")[4][:-4]))
    
    def GameOverAnimation(self, i = 0):
        if i == len(self.frames):
            return
        image = ctk.CTkImage(light_image=Image.open(self.frames[i]), dark_image=Image.open(self.frames[i]), size=(640,360))
        self.configure(image=image)
        self.parent.after(self.delay, lambda: self.GameOverAnimation((i + 1)))

if __name__ == "__main__":
    root = ctk.CTk()
    zyy = Player(root, "./assets/Animation_Game Over/default_player", 10)
    zyy.pack()
    zyy.GameOverAnimation()
    root.mainloop()
