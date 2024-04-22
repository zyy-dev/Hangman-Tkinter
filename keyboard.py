from customtkinter import *

class Keyboard(CTkFrame):
    def __init__ (self, parent: object) -> None:
        super().__init__(master=parent, fg_color="transparent")
        
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
        

        Lower_Button_Frame = CTkFrame(self, fg_color="transparent")
        Lower_Button_Frame.pack(pady=(5, 10))
        for char in "NOPQRSTUVWXYZ":
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
            
            # Using default arguments in lambda functions is a way to capture the value of a variable at the time the lambda function is defined.
        
        parent.bind("<Key>", self.key_pressed)
        
    def on_hover(self, btn: object, event) -> None:
        btn.configure(text_color="#350a66")
        btn.configure(fg_color="#e757bc")
        event.widget.configure(cursor="hand2")

        
    def off_hover(self, btn: object, event) -> None:
        btn.configure(text_color="#FFFFFF")
        btn.configure(fg_color="#520CA1")
        event.widget.configure(cursor="")
        
    def clicked(self, btn: object) -> None:
        btn.unbind("<Enter>")
        btn.unbind("<Leave>")
        btn.configure(state="disabled")
        btn.configure(fg_color="#2f1947")
        btn.configure(text_color="#7A7381")
        
        # if wrong key
        btn.configure(border_width=1)
        btn.configure(border_color="red")
        
    def key_pressed(self, event) -> None:
        if event.char.lower() == 'a': self.clicked(self.btn_a)
        if event.char.lower() == 'b': self.clicked(self.btn_b)
        if event.char.lower() == 'c': self.clicked(self.btn_c)
        if event.char.lower() == 'd': self.clicked(self.btn_d)
        if event.char.lower() == 'e': self.clicked(self.btn_e)
        if event.char.lower() == 'f': self.clicked(self.btn_f)
        if event.char.lower() == 'g': self.clicked(self.btn_g)
        if event.char.lower() == 'h': self.clicked(self.btn_h)
        if event.char.lower() == 'i': self.clicked(self.btn_i)
        if event.char.lower() == 'j': self.clicked(self.btn_j)
        if event.char.lower() == 'k': self.clicked(self.btn_k)
        if event.char.lower() == 'l': self.clicked(self.btn_l)
        if event.char.lower() == 'm': self.clicked(self.btn_m)
        if event.char.lower() == 'n': self.clicked(self.btn_n)
        if event.char.lower() == 'o': self.clicked(self.btn_o)
        if event.char.lower() == 'p': self.clicked(self.btn_p)
        if event.char.lower() == 'q': self.clicked(self.btn_q)
        if event.char.lower() == 'r': self.clicked(self.btn_r)
        if event.char.lower() == 's': self.clicked(self.btn_s)
        if event.char.lower() == 't': self.clicked(self.btn_t)
        if event.char.lower() == 'u': self.clicked(self.btn_u)
        if event.char.lower() == 'v': self.clicked(self.btn_v)
        if event.char.lower() == 'w': self.clicked(self.btn_w)
        if event.char.lower() == 'x': self.clicked(self.btn_x)
        if event.char.lower() == 'y': self.clicked(self.btn_y)
        if event.char.lower() == 'z': self.clicked(self.btn_z)