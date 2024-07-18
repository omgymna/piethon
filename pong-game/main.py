import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor('black')
screen.setup(width = 800,height = 600)
screen.tracer(0)
screen.title("My Pong Game")

scoreboard = ScoreBoard()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))


screen.listen()

screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(l_paddle.go_up, "w")


ball = Ball()

game_is_on = True
while game_is_on:

    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    
    #detecting collision with ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    #detecting collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
    
    #detecting missed ball on right paddle
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.add_left()


    #detect left paddle misses
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.add_right()


screen.exitonclick()