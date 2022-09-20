import turtle as turtle_module
import random

turtle_module.colormode(255)
ask = turtle_module.Turtle()
color_list = [(234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23), (21, 188, 230), (238, 169, 157), (162, 210, 182), (138, 210, 232), (0, 123, 54), (88, 130, 182), (180, 187, 211)]
ss = turtle_module.Screen()
ask.hideturtle()
ask.setheading(225)
ask.penup()
ask.fd(300)
ask.setheading(0)
number_of_dots = 100
ask.speed(0)
for dot_count in range(1, number_of_dots+1):
    ask.dot(20, random.choice(color_list))
    ask.fd(50)

    if dot_count % 10 == 0:
        ask.setheading(90)
        ask.fd(50)
        ask.setheading(180)
        ask.forward(500)
        ask.setheading(0)




ss.exitonclick()