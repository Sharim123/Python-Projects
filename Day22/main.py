from paddle import Paddle
from turtle import Screen, Turtle
from ball import Ball
import time
from scoreboard import Scoreboard

paddle = Turtle()
s = Screen()
scoreboard = Scoreboard()


s.setup(height=600, width=800)
s.bgcolor('black')
s.title('Pong')
s.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

s.listen()
s.onkey(r_paddle.go_up,'Up')
s.onkey(r_paddle.go_down, 'Down')
s.onkey(l_paddle.go_up,'w')
s.onkey(l_paddle.go_down, 's')



game_on = True
while game_on:
    time.sleep(0.1)
    s.update()
    ball.move()

    if ball.xcor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.distance(r_paddle) <  50 and ball.xcor() > 320 or ball.distance(l_paddle)  < 50 and ball.xcor() > -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



s.exitonclick()