from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
speed_level = [0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01]

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(speed_level[score_board.return_speed()])
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.write_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > 295
        or snake.head.xcor() < -295
        or snake.head.ycor() > 295
        or snake.head.ycor() < -295
    ):
        score_board.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            score_board.reset()
            snake.reset()


screen.exitonclick()
