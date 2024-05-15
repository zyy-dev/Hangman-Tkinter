from customtkinter import CTkLabel, CTkImage
from PIL import Image
import os
from Frames.game_play.components.audio import play_audio

class Player(CTkLabel):
    def __init__(self, parent: object, folder_path_gameover :str, folder_path_mistake: str, width: int, height: int, character_object: object, delay: int = 11) -> None:
        super().__init__(master = parent, text="")
        self.folder_path_gameover = folder_path_gameover
        self.folder_path_mistake = folder_path_mistake
        self.width = width
        self.height = height
        self.parent = parent
        self.delay = delay
        self.character_object = character_object
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
        image = CTkImage(light_image=Image.open(self.images_path_mistake[mistakes]), dark_image=Image.open(self.images_path_mistake[mistakes]), size=(self.width,self.height))
        self.configure(image=image)
    
    def GameOverAnimation(self, i=0):
        if i == 0: 
            play_audio.lose()
            self.character_object.time.active = False
            try:
                self.character_object.lbl_skill_1.unbind("<Button-1>")
                self.character_object.lbl_skill_2.unbind("<Button-1>")
            except:
                pass
        if i < len(self.images_path_gameover):
            image = CTkImage(light_image=Image.open(self.images_path_gameover[i]), dark_image=Image.open(self.images_path_gameover[i]), size=(self.width,self.height))
            self.configure(image=image)
            self.after(self.delay, lambda i=i+1: self.GameOverAnimation(i))
        



