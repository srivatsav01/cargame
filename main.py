import time
import turtle
from turtle import Turtle, Screen
from player import Player
from car_manager import  CarManager
from scoreboard import  Scoreboard


screen = Screen()
screen.setup(600,500)
screen.bgcolor("white")
screen.tracer(0)


player = Player()


cars = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.generate_car()
    cars.moving_cars()
    for car in cars.all_cars:
        if player.distance(car)<20:
            game_is_on = False
            scoreboard.game_over()
        if player.ycor()>250:
            player.level_up()
            scoreboard.update_score()
            cars.level_up()
















screen.exitonclick()
