import tkinter as tk

def on_enter(event):
    print("Mouse entered the widget")
    print (event)

def on_leave(event):
    print("Mouse left the widget")

root = tk.Tk()
label = tk.Label(root, text="Hover over me")
label.pack()

label.bind("<Enter>", lambda e: on_enter(e, i))
label.bind("<Leave>", on_leave)

root.mainloop()
