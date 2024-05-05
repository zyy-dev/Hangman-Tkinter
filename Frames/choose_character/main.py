from customtkinter import *
from PIL import Image
from Frames.game.characters.default import default_character, slide_frame
from Frames.game.characters.allan import allan_character
from Frames.game.characters.zyrus import zyrus_character
from Frames.game.characters.richard import richard_character
from Frames.game.characters.renzo import renzo_character
from Frames.game.characters.france import france_character
from Frames.game.components.hover_frame import hover_frame

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
        
        self.character_information_frame = slide_frame(self, 1, 0.55, 1000)
        self.character_information_frame.animate_upwards()
        
        self.sub_frm = CTkFrame(self.character_information_frame, corner_radius=0, fg_color="transparent", border_width=0, width=980, height=250)
        self.sub_frm.pack_propagate(False)
        self.sub_frm.pack(pady=5)
        
        CTkLabel(self.sub_frm, text="The Default Guy", font=("courier", -30, "bold")).pack(pady=10)
        
        # play button
        btn_play = CTkButton(self,
                            text="Play!", 
                            font=("courier", -18, "bold"),
                            corner_radius=0,
                            border_width=0,
                            width=200,
                            height=30,
                            fg_color="#E6D439",
                            text_color="#110320",
                            command=self.play)
        
        btn_play.bind("<Enter>", lambda e : self.on_hover(e, btn_play))
        btn_play.bind("<Leave>", lambda e: self.off_hover(e, btn_play))
        
        self.after(500, lambda: btn_play.place(anchor="s", relx=0.5, rely=0.95))
        
        parent.bind('<Return>', lambda e: self.play())
        parent.bind('<Left>', lambda e: self.left())
        parent.bind('<Right>', lambda e: self.right())

    def right(self):
        if self.index == len(self.image_paths) - 1:
            self.index = 0
        else:
            self.index += 1
        self.image = CTkImage(light_image=Image.open(self.image_paths[self.index]), dark_image=Image.open(self.image_paths[self.index]), size=(self.width, self.height))
        self.lbl.configure(image=self.image)
        self.config_skill_showcase(self.index)
    
    def left(self):
        if self.index == 0:
            self.index = len(self.image_paths) - 1
        else:
            self.index -= 1
        self.image = CTkImage(light_image=Image.open(self.image_paths[self.index]), dark_image=Image.open(self.image_paths[self.index]), size=(self.width, self.height))
        self.lbl.configure(image=self.image)
        self.config_skill_showcase(self.index)
    
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
            zyrus = zyrus_character(self.parent, self.width, self.height, "./assets/Characters/zyrus/game_over", "./assets/Characters/zyrus/wrong_answer", "zyrus")
            self.character_information_frame.animate_downwards()
            # self.after(500, lambda: zyrus.pack())
            # self.pack_forget()
            
    def config_skill_showcase(self, index: int) -> None:
        if index == 0:
            self.sub_frm.pack_forget()
            
            self.sub_frm = CTkFrame(self.character_information_frame, corner_radius=0, fg_color="transparent", border_width=0, width=980, height=1000)
            self.sub_frm.pack_propagate(False)
            self.sub_frm.pack(pady=5)
        
            CTkLabel(self.sub_frm, text="The Default Guy", font=("courier", -30, "bold")).pack(pady=10)
        
        if index == 1:
            self.sub_frm.pack_forget()
            
            self.sub_frm = CTkFrame(self.character_information_frame, corner_radius=0, fg_color="transparent", border_width=0, width=980, height=1000)
            self.sub_frm.pack_propagate(False)
            self.sub_frm.pack(pady=10)
            
            # Character name
            CTkLabel(self.sub_frm, text="Allan", font=("courier", -30, "bold")).pack(pady=(5, 0))
            
            # Frame for skill 1 showcase
            frm1 = CTkFrame(self.sub_frm, fg_color="transparent")
            frm1.pack(pady=5)
            
            # Skill icon/image for skill 1
            logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/allan/skills_icon/skill_1.png"), dark_image=Image.open("./assets/Characters/allan/skills_icon/skill_1.png"), size=(85, 85))
            lbl_skill_1 = CTkLabel(frm1, text="", image=logo_skill_1)
            lbl_skill_1.pack(side="left")
            
            # skill 1 information
            hover_frame(frm1, 780, 90, 1, "allan").pack(side="left", padx=20)
            
            
            # Frame for skill 2 showcase
            frm2 = CTkFrame(self.sub_frm, fg_color="transparent")
            frm2.pack(pady=5)
            
            # Skill icon/image for skill 2
            logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/allan/skills_icon/skill_2.png"), dark_image=Image.open("./assets/Characters/allan/skills_icon/skill_2.png"), size=(85, 85))
            lbl_skill_2 = CTkLabel(frm2, text="", image=logo_skill_2)
            lbl_skill_2.pack(side="left")
            
            # skill 2 information
            hover_frame(frm2, 780, 90, 2, "allan").pack(side="left", padx=20)
            
        if index == 2:
            self.sub_frm.pack_forget()
            
            self.sub_frm = CTkFrame(self.character_information_frame, corner_radius=0, fg_color="transparent", border_width=0, width=980, height=1000)
            self.sub_frm.pack_propagate(False)
            self.sub_frm.pack(pady=10)
            
            # Character name
            CTkLabel(self.sub_frm, text="Renzo", font=("courier", -30, "bold")).pack(pady=(5, 0))
            
            # Frame for skill 1 showcase
            frm1 = CTkFrame(self.sub_frm, fg_color="transparent")
            frm1.pack(pady=5)
            
            # Skill icon/image for skill 1
            logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/renzo/skills_icon/skill_1.jpg"), dark_image=Image.open("./assets/Characters/renzo/skills_icon/skill_1.jpg"), size=(85, 85))
            lbl_skill_1 = CTkLabel(frm1, text="", image=logo_skill_1)
            lbl_skill_1.pack(side="left")
            
            # skill 1 information
            hover_frame(frm1, 780, 90, 1, "renzo").pack(side="left", padx=20)
            
            
            # Frame for skill 2 showcase
            frm2 = CTkFrame(self.sub_frm, fg_color="transparent")
            frm2.pack(pady=5)
            
            # Skill icon/image for skill 2
            logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/renzo/skills_icon/skill_2.jpg"), dark_image=Image.open("./assets/Characters/renzo/skills_icon/skill_2.jpg"), size=(85, 85))
            lbl_skill_2 = CTkLabel(frm2, text="", image=logo_skill_2)
            lbl_skill_2.pack(side="left")
            
            # skill 2 information
            hover_frame(frm2, 780, 90, 2, "renzo").pack(side="left", padx=20)
            
        if index == 3:
            self.sub_frm.pack_forget()
            
            self.sub_frm = CTkFrame(self.character_information_frame, corner_radius=0, fg_color="transparent", border_width=0, width=980, height=1000)
            self.sub_frm.pack_propagate(False)
            self.sub_frm.pack(pady=10)
            
            # Character name
            CTkLabel(self.sub_frm, text="France", font=("courier", -30, "bold")).pack(pady=(5, 0))
            
            # Frame for skill 1 showcase
            frm1 = CTkFrame(self.sub_frm, fg_color="transparent")
            frm1.pack(pady=5)
            
            # Skill icon/image for skill 1
            logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/france/skills_icon/skill_1.png"), dark_image=Image.open("./assets/Characters/france/skills_icon/skill_1.png"), size=(85, 85))
            lbl_skill_1 = CTkLabel(frm1, text="", image=logo_skill_1)
            lbl_skill_1.pack(side="left")
            
            # skill 1 information
            hover_frame(frm1, 780, 90, 1, "france").pack(side="left", padx=20)
            
            
            # Frame for skill 2 showcase
            frm2 = CTkFrame(self.sub_frm, fg_color="transparent")
            frm2.pack(pady=5)
            
            # Skill icon/image for skill 2
            logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/france/skills_icon/skill_2.png"), dark_image=Image.open("./assets/Characters/france/skills_icon/skill_2.png"), size=(85, 85))
            lbl_skill_2 = CTkLabel(frm2, text="", image=logo_skill_2)
            lbl_skill_2.pack(side="left")
            
            # skill 2 information
            hover_frame(frm2, 780, 90, 2, "france").pack(side="left", padx=20)
            
        if index == 4:
            self.sub_frm.pack_forget()
            
            self.sub_frm = CTkFrame(self.character_information_frame, corner_radius=0, fg_color="transparent", border_width=0, width=980, height=1000)
            self.sub_frm.pack_propagate(False)
            self.sub_frm.pack(pady=10)
            
            # Character name
            CTkLabel(self.sub_frm, text="Richard", font=("courier", -30, "bold")).pack(pady=(5, 0))
            
            # Frame for skill 1 showcase
            frm1 = CTkFrame(self.sub_frm, fg_color="transparent")
            frm1.pack(pady=5)
            
            # Skill icon/image for skill 1
            logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/richard/skills_icon/skill_1.jpeg"), dark_image=Image.open("./assets/Characters/richard/skills_icon/skill_1.jpeg"), size=(85, 85))
            lbl_skill_1 = CTkLabel(frm1, text="", image=logo_skill_1)
            lbl_skill_1.pack(side="left")
            
            # skill 1 information
            hover_frame(frm1, 780, 90, 1, "richard").pack(side="left", padx=20)
            
            
            # Frame for skill 2 showcase
            frm2 = CTkFrame(self.sub_frm, fg_color="transparent")
            frm2.pack(pady=5)
            
            # Skill icon/image for skill 2
            logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/richard/skills_icon/skill_2.jpeg"), dark_image=Image.open("./assets/Characters/richard/skills_icon/skill_2.jpeg"), size=(85, 85))
            lbl_skill_2 = CTkLabel(frm2, text="", image=logo_skill_2)
            lbl_skill_2.pack(side="left")
            
            # skill 2 information
            hover_frame(frm2, 780, 90, 2, "richard").pack(side="left", padx=20)
            
        if index == 5:
            self.sub_frm.pack_forget()
            
            self.sub_frm = CTkFrame(self.character_information_frame, corner_radius=0, fg_color="transparent", border_width=0, width=980, height=1000)
            self.sub_frm.pack_propagate(False)
            self.sub_frm.pack(pady=10)
            
            # Character name
            CTkLabel(self.sub_frm, text="Zyrus", font=("courier", -30, "bold")).pack(pady=(5, 0))
            
            # Frame for skill 1 showcase
            frm1 = CTkFrame(self.sub_frm, fg_color="transparent")
            frm1.pack(pady=5)
            
            # Skill icon/image for skill 1
            logo_skill_1 = CTkImage(light_image=Image.open("./assets/Characters/zyrus/skills_icon/skill_1.jpg"), dark_image=Image.open("./assets/Characters/zyrus/skills_icon/skill_1.jpg"), size=(85, 85))
            lbl_skill_1 = CTkLabel(frm1, text="", image=logo_skill_1)
            lbl_skill_1.pack(side="left")
            
            # skill 1 information
            hover_frame(frm1, 780, 90, 1, "richard").pack(side="left", padx=20)
            
            
            # Frame for skill 2 showcase
            frm2 = CTkFrame(self.sub_frm, fg_color="transparent")
            frm2.pack(pady=5)
            
            # Skill icon/image for skill 2
            logo_skill_2 = CTkImage(light_image=Image.open("./assets/Characters/zyrus/skills_icon/skill_2.jpg"), dark_image=Image.open("./assets/Characters/zyrus/skills_icon/skill_2.jpg"), size=(85, 85))
            lbl_skill_2 = CTkLabel(frm2, text="", image=logo_skill_2)
            lbl_skill_2.pack(side="left")
            
            # skill 2 information
            hover_frame(frm2, 780, 90, 2, "richard").pack(side="left", padx=20)
        
    def on_hover(self, event, btn):
        btn.configure(
                    text_color="white",
                    fg_color="#520ca1",
                    font=("", -19, "bold"))
    
    
    def off_hover(self, event, btn):
        btn.configure(
                        text_color="#110320",
                        fg_color="#E6D439",
                        font=("", -18, "bold"))
            
            
                
        