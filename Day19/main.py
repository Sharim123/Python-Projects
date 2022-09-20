from turtle import Turtle, Screen
import random


s = Screen()

is_race_on = False
s.setup(width=500, height=400)
user_guess = s.textinput(title='Race', prompt='Who d you think will win? Enter a color: ')
colors = ['red', 'yellow', 'violet', 'indigo', 'blue', 'orange', 'green']
print(user_guess)
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_guess:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")



        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)







s.exitonclick()