from customtkinter import *
import sqlite3
from datetime import datetime
from PIL import Image
# from start import app
date = datetime.now().strftime("%d/%m/%y")
conn = sqlite3.connect('./Frames/leaderboards/leaderboards.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS scores ('
               'Id INTEGER PRIMARY KEY,'
               'Name TEXT NOT NULL,'
               'Score INTEGER NOT NULL,'
               'Character TEXT NOT NULL,'
               'Date TEXT NOT NULL)')

cursor.execute("SELECT Score FROM scores ORDER BY Score DESC LIMIT 1")
data = cursor.fetchone()
if data == None:
    data = [(0)]


class game_over(CTkFrame):
    def __init__(self, parent, keyboard, time, storage, character, guess, mainmenu_callback, choose_callback):
        super().__init__(master= parent , width= 800, height= 600, border_width= 4, fg_color= "#110320", border_color= "violet")
        self.points = storage
        self.keyboard = keyboard
        self.time = time
        self.main_tk = parent
        self.character = character
        self.guess = guess
        self.mainmenu_callback = mainmenu_callback
        self.choose_callback = choose_callback
        print (self.points)

        self.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.pack_propagate(False)
        

        CTkLabel(self, text= "Game Over!", font=("Times", 120), bg_color="#110320").pack(pady=50)

        self.score_frame = CTkFrame(self, bg_color="#110320", fg_color="#110320")
        self.score_frame.pack(pady=20)
        
        CTkLabel(self.score_frame, text= "Your Score: ", font= ("Times", 30), bg_color="#110320", fg_color="#110320").grid(row=0, column=0, sticky="w")
        CTkLabel(self.score_frame, text= f"{sum(self.points)}", font= ("Times", 30), bg_color="#110320", fg_color="#110320").grid(row=0, column=1, sticky="w")
        
        CTkLabel(self.score_frame, text= "Best Score: ", font= ("Times", 30), bg_color="#110320", fg_color="#110320").grid(row=1, column=0, sticky="w")
        CTkLabel(self.score_frame, text= f"{sum(self.points) if sum(self.points) > data[0] else data[0]}", font= ("Times" , 30), bg_color="#110320", fg_color="#110320").grid(row=1, column=1, sticky="w")
  
        self.name_frame = CTkFrame(self, bg_color="#110320", fg_color="#110320")
        self.name_frame.pack(pady=30)

        CTkLabel(self.name_frame, text="Enter your name:", bg_color="#110320", fg_color="#110320", font=("Times", 20)).grid(row=0, column=0, sticky="w")
        self.name_entry = CTkEntry(self.name_frame, width=200, bg_color="#110320")
        self.name_entry.grid(row=0, column=1, sticky="w")
        self.name_entry.focus_set()
  
        self.save_button = CTkButton(self.name_frame, text="Save", fg_color="#520CA1", text_color="#ffffff", width=45, font=("", -16, "bold"), corner_radius=5, command=self.save_name)
        self.save_button.grid(row=1, column=1)
        self.save_button.bind("<Enter>", lambda e: self.on_hover(e))
        self.save_button.bind("<Leave>", lambda e: self.off_hover(e))
        
        self.interactable_frame = CTkFrame(self, fg_color="#110320")
        self.interactable_frame.pack(pady = 20)
        
        self.icon = Image.open("./assets/Icons/reload.png")
        self.python_icon = CTkImage(light_image=self.icon, dark_image=self.icon)
        self.icon_btn = CTkButton(self.interactable_frame, text="", image=self.python_icon, bg_color="#110320", fg_color="#110320", width=20, command=self.restart)
        self.icon_btn.pack(side= LEFT, padx = 50)

        self.icon2 = Image.open("./assets/Icons/menu-button.png")
        self.python_icon2 = CTkImage(light_image=self.icon2, dark_image=self.icon2)
        self.icon_btn2 = CTkButton(self.interactable_frame, text="", image=self.python_icon2, bg_color="#110320", fg_color="#110320", width=10, command=self.return_to_mainmenu)
        self.icon_btn2.pack(side= LEFT, padx = 50)
        
        
    def on_hover(self, e):
        self.save_button.configure(text_color="#350a66", fg_color="#e757bc")
        
        
    def off_hover(self, e):
        self.save_button.configure(text_color="#FFFFFF", fg_color="#520CA1")

    def save_name(self):
        notif = CTkLabel(self, text=f"Score Saved!", font=("", -18, "bold"), fg_color="green")
        notif.place(relx=0.5, rely=0.5, anchor="center")
        notif.after(2000, lambda: notif.destroy())
        
        self.save_button.configure(state="disabled")
        
        name = self.name_entry.get()
        cursor.execute(
            f'INSERT INTO scores (Name, Score, Character, Date) VALUES  (?, ?, ?, ?)',(name, sum(self.points), self.character, date))

        conn.commit()
        # cursor.execute('SELECT Name, Score FROM scores ORDER BY Score DESC LIMIT 5')
        cursor.execute(f"SELECT Score, RANK() OVER (ORDER BY Score DESC) Ranking FROM scores")
        data = cursor.fetchall()

    def restart(self):
        self.destroy()
        self.points.clear()
        self.guess.current_level = 0
        self.keyboard.reset()

        self.keyboard.character_object.destroy()
        self.choose_callback.play()
        
        self.time.seconds = 200
        self.time.active = True
        self.time.activate_time()
    def return_to_mainmenu(self):
        self.points.clear()
        self.guess.current_level = 0
        self.keyboard.character_object.destroy()
        self.mainmenu_callback()
        self.destroy()
        