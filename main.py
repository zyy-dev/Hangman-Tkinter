from customtkinter import *
from animation import Player
from keyboard import Keyboard
from guess import Guess
from words import word_to_guess

app = CTk()

# window settings
width = app.winfo_screenwidth()
height = app.winfo_screenheight()       
app.geometry(f"{width}x{height}+-11+-5")
app.minsize(width, height)
set_appearance_mode("dark")
app.title("Hangman")

# assemble
default = Player(app, "./assets/Animation_Game Over/default_player", "./assets/Animation_Wrong Answer/default_player")
default.place(rely=0.05, relx=0.5, anchor="n")

random_word = word_to_guess.lvl_1()
CTkLabel(app, text=random_word[0], font=("", -17, "bold")).place(rely=0.64, relx=0.5, anchor="n")

guess = Guess(app, random_word[1])
guess.place(rely=0.7, relx=0.5, anchor="n")

keyboard = Keyboard(app, guess, default) #connects the guess and animation module to keyboard
keyboard.place(rely=0.8, relx=0.5, anchor="n")

# run
app.mainloop()