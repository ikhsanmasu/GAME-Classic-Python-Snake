from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_left, "Left")
screen.onkeypress(snake.move_right, "Right")


food = Food(snake)
score = Score()


game_is_on = True
while game_is_on:
    snake.move_forward()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            score.update_highscore()
            snake.reset()
            score.reset()

    if not (-300 < snake.head.xcor() < 300) or not (-300 < snake.head.ycor() < 300):
        score.update_highscore()
        snake.reset()
        score.reset()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend_segment()
        score.update_score()
        score.update_highscore()

    screen.update()
    sleep(0.1)

screen.exitonclick()
