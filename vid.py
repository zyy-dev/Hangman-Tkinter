from customtkinter import *
from tkinter import *
from tkvideo import tkvideo

root = CTk()
root.title("Video Player")
set_appearance_mode("dark")
# Create a tkvideo instance

# Create a Tkinter label and attach the tkvideo instance
player_label = Label(root)
player = tkvideo(path =r".\assets\open.mp4",
                 loop=False, label=player_label,  size=(root.winfo_screenwidth(),root.winfo_screenheight()))
player_label.pack()

# overlay_btn = tk.Button(root, text= "Hello I am OverLaid!").pack()
# Play the video
player.play()

root.mainloop()