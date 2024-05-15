from customtkinter import CTkLabel, CTkImage
from PIL import Image
import os

class Animation(CTkLabel):
    def __init__(self, parent: object, folder_path :str, width=640, height=360, delay = 11) -> None:
        super().__init__(master = parent, text="")
        self.folder_path = folder_path
        self.width = width
        self.height = height
        self.parent = parent
        self.delay = delay
        self.frames = self.import_images()
        self.animate()
        
    def import_images(self) -> list[str]:
        image_paths = []
        for file_name in os.listdir(self.folder_path):
            image_paths.append(self.folder_path + "/" + file_name)
        index = int(list(self.folder_path).count("/")) + 1
        return sorted(image_paths, key= lambda item: int(item.split("/")[index][:-4]))
    
    # recursion
    def animate(self, i = 0):
        if i == len(self.frames):
            return
        image = CTkImage(light_image=Image.open(self.frames[i]), dark_image=Image.open(self.frames[i]), size=(self.width,self.height))
        self.configure(image=image)
        self.image = image
        self.parent.after(self.delay, lambda: self.animate((i + 1)))
        
        