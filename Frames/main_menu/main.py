from customtkinter import *
from animation import Animation

class MainMenu(CTkFrame):
    def __init__(self, parent: object, width: int, height: int, start_game_callback):
        super().__init__(master=parent, width=width, height=height)

        default = Animation(self, "./assets/Animation_Open App", width, height)
        default.pack()
        
        self.after(1000, lambda: self.place_button())
        
        self.btn_play = CTkButton(self, text="Start Game", 
                             font=("", -18, "bold"),
                             corner_radius=0,
                             border_width=0,
                             width=200,
                             height=40,
                             fg_color="#E6D439",
                             text_color="#110320",
                             command=start_game_callback)
        self.btn_play.bind("<Enter>", lambda e : self.on_hover(e, self.btn_play))
        self.btn_play.bind("<Leave>", lambda e: self.off_hover(e, self.btn_play))
        parent.bind('<Return>', lambda e: start_game_callback())

        self.btn_score = CTkButton(self, text="Leaderboards", 
                             font=("", -18, "bold"),
                             corner_radius=0,
                             border_width=0,
                             width=200,
                             height=40,
                             fg_color="#E6D439",
                             text_color="#110320")
        self.btn_score.bind("<Enter>", lambda e : self.on_hover(e, self.btn_score))
        self.btn_score.bind("<Leave>", lambda e: self.off_hover(e, self.btn_score))
        
        self.btn_quit = CTkButton(self, text="Quit", 
                             font=("", -18, "bold"),
                             corner_radius=0,
                             border_width=0,
                             width=200,
                             height=40,
                             fg_color="#E6D439",
                             text_color="#110320",
                             command=lambda: exit())
        self.btn_quit.bind("<Enter>", lambda e : self.on_hover(e, self.btn_quit))
        self.btn_quit.bind("<Leave>", lambda e: self.off_hover(e, self.btn_quit))
        parent.bind('<Escape>', lambda e: exit())
        
    
    def place_button(self):
        self.btn_play.place(relx=0.5, rely=0.5, anchor="center")
        self.btn_score.place(relx=0.5, rely=0.58, anchor="center")
        self.btn_quit.place(relx=0.5, rely=0.66, anchor="center")
        
    def on_hover(self, event, btn):
        btn.configure(width=215,
                      height=48,
                      text_color="white",
                      fg_color="#520ca1",
                      font=("", -19, "bold"))
        
        
    def off_hover(self, event, btn):
        btn.configure(width=200,
                      height=40,
                      text_color="#110320",
                      fg_color="#E6D439",
                      font=("", -18, "bold"))
        
