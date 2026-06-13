from turtle import Turtle,Screen
import time

from food import Food
from snake import Snake
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game ")
screen.tracer(0)

game_on = True
snake = Snake()
food = Food()
sb = Scoreboard()


screen.listen()
screen.onkey(snake.right,"Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        sb.increase_score()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        sb.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            sb.reset()
            snake.reset()



screen.exitonclick()