from turtle import Turtle, Screen

from ball import Ball
from paddle import Paddle
import time

from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)

ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on = True
while(game_is_on):
    sleep_time = 0.1
    time.sleep(sleep_time)
    screen.update()
    ball.move()
    scoreboard.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        sleep_time *= 0.9


    if ball.xcor() > 380:
        sleep_time = 0.1
        ball.reset()
        scoreboard.l()

    if ball.xcor() < -380:
        sleep_time = 0.1
        ball.reset()
        scoreboard.r()

    if scoreboard.score():
        break


screen.exitonclick()