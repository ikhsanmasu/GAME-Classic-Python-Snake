from turtle import Turtle

import os
import sys

# # use this directory when generating exe file
# if getattr(sys, 'frozen', False):
#     # If the application is run as a bundle, the PyInstaller bootloader
#     # extends the sys module by a flag frozen=True and sets the app
#     # path into variable _MEIPASS'.
#     application_path = sys._MEIPASS
# else:
#     application_path = os.path.dirname(os.path.abspath(__file__))
#
# csv_dir = application_path + "/score.txt"

csv_dir = "score.txt"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as file:
            self.highest_score = file.read()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.write_score()

    def write_highscore(self):
        with open("score.txt") as file:
            self.highest_score = file.read()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score : {self.score} Highest Score : {self.highest_score}", align="center", font=("Arial", 15, "normal"))

    def update_score(self):
        self.score += 1
        self.write_score()
        self.write_highscore()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=("Arial", 20, "normal"))

    def update_highscore(self):
        if self.score > int(self.highest_score):
            with open("score.txt", mode="w") as file:
                file.write(f"{self.score}")
            self.write_score()
            self.write_highscore()

    def reset(self):
        self.score = 0
        self.write_score()

