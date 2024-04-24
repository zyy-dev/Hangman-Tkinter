from customtkinter import *
import time

class Keyboard(CTkFrame):
    def __init__ (self, parent: object, guess: object, animation: object) -> None:
        super().__init__(master=parent, fg_color="transparent")
        self.parent = parent
        self.guess = guess
        self.animation = animation
        self.mistakes = 0
        self.correct = 0
        self.button_address = {}
                            # key: character
                            # value: reference address of Button Widgets
        
        Upper_Button_Frame = CTkFrame(self, fg_color="transparent")
        Upper_Button_Frame.pack(pady=8)
        for char in "ABCDEFGHIJKLMN":
            btn = CTkButton(Upper_Button_Frame, 
                            text=char, 
                            width=45,
                            height=30, 
                            fg_color="#520CA1", 
                            corner_radius=5, 
                            text_color="#FFFFFF", 
                            font=("", -16, "bold"))
            
            btn.pack(side="left", padx=8)
            btn.bind("<Enter>", lambda event, btn=btn: self.on_hover(btn, event))
            btn.bind("<Leave>", lambda event, btn=btn: self.off_hover(btn, event)) 
            btn.configure(command=lambda btn=btn: self.clicked(btn))
            self.button_address[char] = btn
        

        Lower_Button_Frame = CTkFrame(self, fg_color="transparent")
        Lower_Button_Frame.pack(pady=8)
        for char in "OPQRSTUVWXYZ":
            btn = CTkButton(Lower_Button_Frame, 
                            text=char, 
                            width=45,
                            height=30, 
                            fg_color="#520CA1", 
                            corner_radius=5, 
                            text_color="#FFFFFF", 
                            font=("Arial", -16, "bold"))
            
            btn.pack(side="left", padx=8)
            btn.bind("<Enter>", lambda event, btn=btn: self.on_hover(btn, event))
            btn.bind("<Leave>", lambda event, btn=btn: self.off_hover(btn, event)) 
            btn.configure(command=lambda btn=btn: self.clicked(btn))
            self.button_address[char] = btn
            
            # Using default arguments in lambda functions is a way to capture the value of a variable at the time the lambda function is defined.
        
        self.parent.bind("<Key>", self.key_pressed)
        
    def on_hover(self, btn: object, event) -> None:
        btn.configure(text_color="#350a66", fg_color="#e757bc")
        
    def off_hover(self, btn: object, event) -> None:
        btn.configure(text_color="#FFFFFF", fg_color="#520CA1")
        
    def clicked(self, btn: object) -> None:
        btn.unbind("<Enter>")
        btn.unbind("<Leave>")
        btn.configure(state="disabled")
        btn.configure(fg_color="#2f1947")
        btn.configure(text_color="#7A7381")

        # if wrong key
        if not self.guess.validate_char(btn.cget("text")):
            btn.configure(border_width=1)
            btn.configure(border_color="red")
            
            self.mistakes += 1
            if self.mistakes > 6:
                btn.configure(state="disabled")
                self.animation.GameOverAnimation()
                self.disabled()
            else:
                self.animation.WrongAnswer(self.mistakes)
        # if correct
        else:
            self.correct += 1
            if self.correct == len(set(self.guess.word_to_guess)):
                self.disabled()
                self.after(2000, self.reset) 
        
        
    def key_pressed(self, event) -> None:
        selected = event.char.upper()
        if selected in self.button_address:
            self.clicked(self.button_address[selected])
            
    def disabled(self):
        self.parent.unbind("<Key>")
        for char in self.button_address:
            self.button_address[char].configure(state="disabled")
            self.button_address[char].unbind("<Enter>")
            self.button_address[char].unbind("<Leave>")
    
    def reset(self):
        self.guess.next_level()
        self.parent.bind("<Key>", self.key_pressed)
        self.mistakes = 0
        self.correct = 0
        for char in self.button_address:                       
            self.button_address[char].configure(state="normal", fg_color="#520CA1", text_color="#FFFFFF")
            self.button_address[char].bind("<Enter>", lambda event, btn=self.button_address[char]: self.on_hover(btn, event))
            self.button_address[char].bind("<Leave>", lambda event, btn=self.button_address[char]: self.off_hover(btn, event)) 
            
            