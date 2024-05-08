from customtkinter import *
import sqlite3
from PIL import Image

conn = sqlite3.connect('./Frames/leaderboards/leaderboards.db')
cursor = conn.cursor()

cursor.execute("Select * FROM scores ORDER BY score DESC")
data = cursor.fetchall()

cursor.execute(f"SELECT Score, RANK() OVER (ORDER BY Score DESC) Ranking FROM scores")
ranked_data = cursor.fetchall()


class Leaderboards(CTkFrame):
    def __init__(self, parent):
        super().__init__(master= parent, width= 800, height= 600,bg_color= "#110320", fg_color= "#110320", border_color= "violet", border_width= 5)
        self.HEIGHT = 600
        self.WIDTH = 800
        self.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.pack_propagate(False)



        leaderboards_frame = CTkFrame(self, fg_color= "#110320")
        leaderboards_lbl = CTkLabel(leaderboards_frame, text= "Leaderboards", font= ("Times", 120) ,bg_color= "#110320")
        leaderboards_lbl.pack(pady = 20)
        leaderboards_frame.pack(pady = 20)


        frame5 = CTkScrollableFrame(self, width=340, height=350, fg_color="#110320" )
        frame5.pack(padx=10, pady=10,fill = "x", expand = TRUE, anchor = CENTER)

        lbl_frame5_rank = CTkLabel(frame5, text="Rank", font=("courier", 20, "bold"))
        lbl_frame5_rank.grid(row=0, column=0, padx=20)
        lbl_frame5_name = CTkLabel(frame5, text="Name", font=("courier", 20, "bold"))
        lbl_frame5_name.grid(row=0, column=1, padx=20)
        lbl_frame5_score = CTkLabel(frame5, text="Score", font=("courier", 20, "bold"))
        lbl_frame5_score.grid(row=0, column=2, padx=20)
        lbl_frame5_score = CTkLabel(frame5, text="Character Played", font=("courier", 20, "bold"))
        lbl_frame5_score.grid(row=0, column=3, padx=20)
        lbl_frame5_score = CTkLabel(frame5, text="Date", font=("courier", 20, "bold"))
        lbl_frame5_score.grid(row=0, column=4, padx=20)




        for num in range(len(data)):
            lbl_frame5_rank_info = CTkLabel(frame5, text= ranked_data[num][1], font=("courier", 20, "bold"))
            lbl_frame5_rank_info.grid(row=num+1, column=0, padx=10, pady=5)
            frame5.grid_columnconfigure(num+1, weight=1)
            lbl_frame5_name_info = CTkLabel(frame5, text=data[num][1],
                                            font=("courier", 20, "bold"))
            lbl_frame5_name_info.grid(row=num+1, column=1, padx=10, pady=5)
            frame5.grid_columnconfigure(num+1, weight=1)
            lbl_frame5_score_info = CTkLabel(frame5, text=data[num][2], font=("courier", 20, "bold"))
            lbl_frame5_score_info.grid(row=num+1, column=2, padx=10, pady=5)
            frame5.grid_columnconfigure(num+1, weight=1)
            lbl_frame5_character_info = CTkLabel(frame5, text=data[num][3], font=("courier", 20, "bold"))
            lbl_frame5_character_info.grid(row=num + 1, column=3, padx=10, pady=5)
            frame5.grid_columnconfigure(num + 1, weight=1)
            lbl_frame5_date_info = CTkLabel(frame5, text=data[num][4], font=("courier", 20, "bold"))
            lbl_frame5_date_info.grid(row=num + 1, column=4, padx=10, pady=5)
            frame5.grid_columnconfigure(num + 1, weight=1)

        icon = Image.open(r"./assets/Leaderboards/exit.png")
        python_icon = CTkImage(light_image= icon, dark_image= icon, size= (80,76))
        icon_btn = CTkButton(self, text="", image=python_icon, fg_color="#110320", width= 80 , height=76, command= self.close_window)
        icon_btn.place(x=695, y=5)
    def close_window(self):
        self.destroy()
