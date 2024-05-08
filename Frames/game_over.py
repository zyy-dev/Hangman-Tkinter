from customtkinter import *
import sqlite3
from datetime import datetime
from PIL import Image, ImageTk
# from start import app
date = datetime.now().strftime("%d/%m/%y")
conn = sqlite3.connect('leaderboards.db')
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


class endScore(CTkFrame):
    def __init__(self, parent, keyboard, time, storage, character, guess, mainmenu_callback):
        super().__init__(master= parent , width= 800, height= 600, border_width= 4, border_color= "violet")
        self.points = storage
        self.keyboard = keyboard
        self.time = time
        self.main_tk = parent
        self.character = character
        self.guess = guess
        self.mainmenu_callback = mainmenu_callback
        self.GAME_OVER_FONT_SIZE = 80
        self.SCORE_FONT_SIZE = 30
        self.VERTICAL_SPACE = 30
        self.HEIGHT = 585
        self.WIDTH = 785
        self.place(relx=0.5, rely=0.5, anchor=CENTER)


        FontManager.load_font(r"./assets/Fonts/Melted Monster.ttf")
        FontManager.load_font(r"./assets/Fonts/Friday13v12.ttf")
        canvas = CTkCanvas(self, width=self.WIDTH, height=self.HEIGHT, bg="#110320")
        canvas.place(relx=0.5, rely=0.5, anchor="center")
        game_over_text = canvas.create_text(self.WIDTH // 2, self.HEIGHT // 3, text="GAME OVER", fill="#E757BC",
                                            font=("MeltedMonster", self.GAME_OVER_FONT_SIZE))

        score_text = canvas.create_text(self.WIDTH // 2 - 50, self.HEIGHT // 2 + self.VERTICAL_SPACE, text="  Score: ",
                                        fill="#FFFFFF",
                                        font=("Friday13v12", self.SCORE_FONT_SIZE))
        score_number_text = canvas.create_text(self.WIDTH // 2 + 50, self.HEIGHT // 2 + self.VERTICAL_SPACE,
                                               text=f"             {sum(self.points) }",
                                               fill="#FFFF00", font=("Friday13v12", self.SCORE_FONT_SIZE))
        best_score_text = canvas.create_text(self.WIDTH // 2 - 80,
                                             self.HEIGHT // 2 + self.SCORE_FONT_SIZE + self.VERTICAL_SPACE,
                                             text="Best score: ", fill="#FFFFFF",
                                             font=("Friday13v12", self.SCORE_FONT_SIZE))
        best_score_number_text = canvas.create_text(self.WIDTH // 2 + 30,
                                                    self.HEIGHT // 2 + self.SCORE_FONT_SIZE + self.VERTICAL_SPACE,
                                                    text=f"                 {sum(self.points) if sum(self.points) > data[0] else data[0]} ", fill="#FFFF00",
                                                    font=("Friday13v12", self.SCORE_FONT_SIZE))

        name_label = CTkLabel(self, text="Enter your name:", bg_color="#110320")
        name_label.place(x=250, y=400)
        name_entry = CTkEntry(self, width=200)
        name_entry.place(x=350, y=400)

        def save_name():
            name = name_entry.get()
            cursor.execute(
                f'INSERT INTO scores (Name, Score, Character, Date) VALUES  (?, ?, ?, ?)',(name, sum(self.points), self.character, date))

            conn.commit()
            # cursor.execute('SELECT Name, Score FROM scores ORDER BY Score DESC LIMIT 5')
            cursor.execute(f"SELECT Score, RANK() OVER (ORDER BY Score DESC) Ranking FROM scores")
            data = cursor.fetchall()
            print(data)
            conn.close()
        save_button = CTkButton(self, text="Save", command=save_name)
        save_button.place(x=400, y=430)

        icon = Image.open(r"./assets/Game Over/reload.png")
        python_icon = CTkImage(light_image= icon, dark_image= icon)
        icon_btn = CTkButton(self, text="", image=python_icon, bg_color="blue", command= self.restart)
        icon_btn.place(x=500, y=500)

        icon2 = Image.open(r"./assets/Game Over/menu-button.png")
        python_icon2 = CTkImage(light_image= icon2, dark_image= icon2)
        icon_btn2 = CTkButton(self, text="", image=python_icon2, bg_color="blue", command= self.return_to_mainmenu)
        icon_btn2.place(x=300, y=500)
    def restart(self):
        self.destroy()
        self.points.clear()
        self.guess.current_level = 0
        self.keyboard.reset()
        self.time.seconds = 200
        self.time.active = True
        self.time.activate_time()
    def return_to_mainmenu(self):
        self.destroy()
        self.points.clear()
        self.guess.current_level = 0
        self.keyboard.character_object.destroy()
        self.mainmenu_callback()