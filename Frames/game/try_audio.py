from customtkinter import *
from playsound import playsound

root = CTk()

check_answer = "some value"

def check_answer_func():
    global check_answer
    if check_answer == "some value":
        playsound("./assets/audios/audios_correct.mp3")
    else:
        wrong()

def wrong():
    playsound("./assets/audios/audios_wrong.mp3")


check_button = CTkButton(root, text="Check Answer", command=check_answer_func)
check_button.pack()

root.mainloop()
