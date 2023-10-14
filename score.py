from turtle import Turtle

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

