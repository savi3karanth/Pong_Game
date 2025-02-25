from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("Black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detects the collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # detects r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detects l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

