from customtkinter import *
from PIL import Image
from animation import AnimatedButton

app = CTk()

# window settings
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
app.geometry(f"{width}x{height}+-11+-5")
app.minsize(width, height)
set_appearance_mode("dark")
app.title("Hangman")

btn = CTkButton(app, text="Button")
btn.pack()

x = AnimatedButton(app, './assets/Animation_Game Over/default_player', './assets/Animation_Game Over/default_player')
x.pack()
x.trigger_animation()
app.mainloop()