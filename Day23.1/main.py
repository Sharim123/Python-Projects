import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

car_manager = CarManager()
scoreboard = Scoreboard()
play = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("TURTLE CROSSING")

screen.listen()
screen.onkey(play.go_up, 'Up')




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    car_manager.create_car()
    car_manager.move_car()


    for car in car_manager.all_cars:
        if car.distance(play) < 20:
            game_is_on = False
            scoreboard.game_over()

    if play.ycor() == play:
        print("You win")


    if play.is_at_finish_line():
        play.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()