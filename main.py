from customtkinter import *
from animation import Player
from keyboard import Keyboard

def mistake():
    global mistakes
    mistakes += 1
    if mistakes > 6:
        btn.configure(state="disabled")
        default.GameOverAnimation()
    else:
        default.WrongAnswer(mistakes)

app = CTk()

# window settings
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
app.geometry(f"{width}x{height}+-11+-5")
app.minsize(width, height)
set_appearance_mode("dark")
app.title("Hangman")

default = Player(app, "./assets/Animation_Game Over/default_player", "./assets/Animation_Wrong Answer/default_player")
default.pack()

mistakes = 0
btn = CTkButton(app, text="Next", command=mistake)
btn.pack(pady=10)

keyboard = Keyboard(app)
keyboard.place(rely=0.8, relx=0.5, anchor="center")









# run
app.mainloop()