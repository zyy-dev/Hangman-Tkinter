from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkToplevel
from animation import Animation
from Frames.game_play.components.audio import play_audio

class MainMenu(CTkFrame):
    def __init__(self, parent: object, width: int, height: int, start_game_callback, leaderboards_callback):
        super().__init__(master=parent, width=width, height=height)
        self.start_game_callback = start_game_callback
        self.leaderboards_callback = leaderboards_callback
        self.parent = parent
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
                             command=self.play)
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
                             text_color="#110320",
                             command=self.score)
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
                             command=self.exit)
        self.btn_quit.bind("<Enter>", lambda e : self.on_hover(e, self.btn_quit))
        self.btn_quit.bind("<Leave>", lambda e: self.off_hover(e, self.btn_quit))
        parent.bind('<Escape>', lambda e: exit())
        
    
    def place_button(self):
        self.btn_play.place(relx=0.5, rely=0.5, anchor="center")
        self.btn_score.place(relx=0.5, rely=0.58, anchor="center")
        self.btn_quit.place(relx=0.5, rely=0.66, anchor="center")
        
    def on_hover(self, event, btn, size:bool = True):
        btn.configure(text_color="white", fg_color="#520ca1",)
        
        if size:
            btn.configure(width=215,
                      height=48,
                      font=("", -19, "bold"))
        
        
    def off_hover(self, event, btn, size:bool = True):
        btn.configure(text_color="#110320", fg_color="#E6D439",)
        
        if size:
             btn.configure(width=200,
                      height=40,
                      font=("", -18, "bold"))
        
    def play(self):
        print ("called")
        play_audio.click()
        self.start_game_callback(True)

    def score(self):
        play_audio.click()
        self.leaderboards_callback()
    def exit(self):
        play_audio.lose()
        self.top_lvl = CTkToplevel(self.parent)
        self.top_lvl.title("Exit the Game")
        self.top_lvl.geometry("500x130")
        self.top_lvl.resizable(False, False)
        self.top_lvl.grab_set()        
        
        CTkLabel(self.top_lvl, text="Are you sure you want to Exit the game?", font=("courier", -19, "bold")).pack(pady=20)

        frm_btn = CTkFrame(self.top_lvl, fg_color="transparent")
        frm_btn.pack(pady=10)
        
        btn1 = CTkButton(frm_btn, text="No", 
                             font=("courier", -15, "bold"),
                             width=130,
                             height=30,
                             fg_color="#E6D439",
                             text_color="#110320",
                             command=self.top_lvl_btn_function)
        btn1.pack(side="left", anchor="center", padx=10)
        btn1.bind("<Enter>", lambda e : self.on_hover(e, btn1, False))
        btn1.bind("<Leave>", lambda e: self.off_hover(e, btn1, False))
        
        btn2 = CTkButton(frm_btn, text="Hindi", 
                             font=("courier", -15, "bold"),
                             width=130,
                             height=30,
                             fg_color="#E6D439",
                             text_color="#110320",
                             command=self.top_lvl_btn_function)
        btn2.pack(side="left", anchor="center", padx=10)
        btn2.bind("<Enter>", lambda e : self.on_hover(e, btn2, False))
        btn2.bind("<Leave>", lambda e: self.off_hover(e, btn2, False))
        
    def top_lvl_btn_function(self):
        play_audio.click()
        self.top_lvl.destroy()