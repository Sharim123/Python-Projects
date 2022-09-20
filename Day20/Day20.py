from turtle import Turtle, Screen
from food import Food
from Saanp import Snake
from scoreboard import Scoreboard
import time

t = Turtle()
a = Turtle()
b = Turtle()
s = Screen()

s.setup(width=600, height=600)
s.bgcolor('black')
s.title('Snakes')
s.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

s.onkey(snake.up, "w")
s.onkey(snake.down, "s")
s.onkey(snake.left, "a")
s.onkey(snake.right, "d")


game_on = True
while game_on:
    s.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        print('khewi')
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()








s.exitonclick()