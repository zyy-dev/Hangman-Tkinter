from customtkinter import *
from Frames.choose_character.main import Choices
from Frames.main_menu.main import MainMenu
from animation import Animation

# main window
app = CTk()

# window settings
width = app.winfo_screenwidth()
height = app.winfo_screenheight()       
app.geometry(f"{width}x{height}+-11+-5")
app.minsize(width, height)
set_appearance_mode("dark")
app.title("Hangman")

def start_game():
    main.pack_forget()
    animation = Animation(app, "./assets/Animation_Start Game", width=width, height=height, delay=20)
    animation.pack()
    app.after(3000, lambda: animation.pack_forget())
    x = Choices(app, width, height)
    x.pack()

main = MainMenu(app, width, height, start_game)
main.pack()

app.mainloop()











# run
app.mainloop()