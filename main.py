from customtkinter import *
from PIL import Image
from animation import Player

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

default = Player(app, "./assets/Animation_Game Over/default_player", "./assets/Animation_Wrong Answer/default_player", 10)
default.pack()

mistakes = 0
btn = CTkButton(app, text="Next", command=mistake)
btn.pack(pady=10)
app.mainloop()