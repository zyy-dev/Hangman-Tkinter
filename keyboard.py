from customtkinter import *

class Keyboard(CTkFrame):
    def __init__ (self, parent: object, connect_to: object) -> None:
        super().__init__(master=parent, fg_color="transparent")
        self.parent = parent
        self.connect_to = connect_to
        self.button_address = {}
                            # key: character
                            # value: reference address of Button Widgets
        
        Upper_Button_Frame = CTkFrame(self, fg_color="transparent")
        Upper_Button_Frame.pack(pady=(10, 5))
        for char in "ABCDEFGHIJKLM":
            btn = CTkButton(Upper_Button_Frame, 
                            text=char, 
                            width=70, 
                            height=40, 
                            fg_color="#520CA1", 
                            corner_radius=5, 
                            text_color="#FFFFFF", 
                            font=("Arial", -16, "bold"))
            
            btn.pack(side="left", padx=5)
            btn.bind("<Enter>", lambda event, btn=btn: self.on_hover(btn, event))
            btn.bind("<Leave>", lambda event, btn=btn: self.off_hover(btn, event)) 
            btn.configure(command=lambda btn=btn: self.clicked(btn))
            self.button_address[char] = btn
        

        Lower_Button_Frame = CTkFrame(self, fg_color="transparent")
        Lower_Button_Frame.pack(pady=(5, 10))
        for char in "NOPQRSTUVWXYZ":
            btn = CTkButton(Lower_Button_Frame, 
                            text=char, 
                            width=70, 
                            height=40, 
                            fg_color="#520CA1", 
                            corner_radius=5, 
                            text_color="#FFFFFF", 
                            font=("Arial", -16, "bold"))
            
            btn.pack(side="left", padx=5)
            btn.bind("<Enter>", lambda event, btn=btn: self.on_hover(btn, event))
            btn.bind("<Leave>", lambda event, btn=btn: self.off_hover(btn, event)) 
            btn.configure(command=lambda btn=btn: self.clicked(btn))
            self.button_address[char] = btn
            
            # Using default arguments in lambda functions is a way to capture the value of a variable at the time the lambda function is defined.
        
        self.parent.bind("<Key>", self.key_pressed)
        
    def on_hover(self, btn: object, event) -> None:
        btn.configure(text_color="#350a66", fg_color="#e757bc")
        event.widget.configure(cursor="hand2")
        
    def off_hover(self, btn: object, event) -> None:
        btn.configure(text_color="#FFFFFF", fg_color="#520CA1")
        event.widget.configure(cursor="")
        
    def clicked(self, btn: object) -> None:
        btn.unbind("<Enter>")
        btn.unbind("<Leave>")
        btn.configure(state="disabled")
        btn.configure(fg_color="#2f1947")
        btn.configure(text_color="#7A7381")
        print(self.connect_to.validate_char(btn.cget("text")))
            # if wrong key
        if not self.connect_to.validate_char(btn.cget("text")):
            btn.configure(border_width=1)
            btn.configure(border_color="red")
        
        
        
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
        
            