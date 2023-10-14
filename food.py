from turtle import Turtle
from random import choice

class Food(Turtle):
    def __init__(self, snake):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.snake = snake
        self.refresh()


    def refresh(self):
        new_x = choice([x for x in range(-280, 280, 20) if x not in self.snake.segment_xposition()])
        new_y = choice([y for y in range(-280, 280, 20) if y not in self.snake.segment_yposition()])
        self.goto(new_x, new_y)