from customtkinter import *
from pages.game.HangMan import HangMan
from pages.main_menu.menu import MainMenu
from animation import Animation

# main window
app = CTk()

# window settings
width = app.winfo_screenwidth()
height = app.winfo_screenheight()       
app.geometry(f"{width}x{height}+-11+-5")
app.minsize(width, height)
set_appearance_mode("light")
app.title("Hangman")

def start_game():
    y.pack_forget()
    animation = Animation(app, "./assets/Animation_Start Game", width=width, height=height, delay=20)
    animation.pack()
    app.after(2000, lambda: animation.pack_forget())
    x = HangMan(app, width, height, app)
    x.pack()

y = MainMenu(app, width, height, start_game)
y.pack()

app.mainloop()











# run
app.mainloop()