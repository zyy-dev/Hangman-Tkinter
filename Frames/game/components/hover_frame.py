from customtkinter import CTkFrame, CTkLabel
from Data.characters_info import characters_info

class hover_frame(CTkFrame):
    def __init__ (self, parent: object, width: int, height: int, skill_number: int, character: str) -> None:
        super().__init__(master=parent, width=width, height=height)
        
        name, description, cooldown = characters_info.skill_info(skill_number, character)
        
        self.pack_propagate(False)
        if skill_number == 1:
            self.place(anchor="e", rely=0.1, relx=0.925)
        if skill_number == 2:
            self.place(anchor="e", rely=0.25, relx=0.925)
        
        CTkLabel(self, text=name, font=("courier", -20, "bold"), text_color="#E6D439").pack(anchor="w", padx=10)
        CTkLabel(self, text=f"Cooldown: {cooldown}", font=("", -12)).pack(anchor="w", padx=10)
        CTkLabel(self, text=description, font=("", -10), justify="left", wraplength=380).pack(anchor="w", padx=10)