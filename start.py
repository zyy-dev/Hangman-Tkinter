from customtkinter import *
from Frames.choose_character import Choices
from Frames.main_menu import MainMenu
from animation import Animation
from Frames.leaderboards import Leaderboards
# main window
class HangmanApp(CTk):
    def __init__(self):
        super().__init__()

        # window settings
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry(f"{self.width}x{self.height}+-11+-5")
        self.minsize(self.width, self.height)
        set_appearance_mode("dark")
        self.title("Hangman")

        self.show_mainmenu()

    def start_game(self):
        self.main_menu.pack_forget()
        animation = Animation(self, "./assets/Animation_Start Game", width=self.winfo_width(),
                              height=self.winfo_height(), delay=20)
        animation.pack()
        x = Choices(self, self.winfo_width(), self.winfo_height(), self.show_mainmenu)
        x.pack()
        self.after(2000, lambda: animation.pack_forget())
    def show_mainmenu(self):
        self.main_menu = MainMenu(self, self.width, self.height, self.start_game, self.show_leaderboards)
        self.main_menu.pack()
    def show_leaderboards(self):
        Leaderboards(self)


# Create an instance of HangmanApp
app = HangmanApp()

# Run the application
app.mainloop()