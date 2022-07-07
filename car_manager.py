from turtle import  Turtle
import random


COLORS = ["red","yellow","orange","green","purple","blue"]

class CarManager:
    def __init__(self):
         self.all_cars = []
         self.game_is_on = True
         self.move_distance = 5
         self.level = 3
    def generate_car(self):
        random_chance = random.randint(1,20)
        if random_chance < self.level:
            new_car = Turtle("square")
            new_car.penup()
            new_car.left(180)
            new_car.shapesize(stretch_wid=1,stretch_len=2.5)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-240,240)
            new_car.hideturtle()
            new_car.goto(340,random_y)
            new_car.showturtle()
            self.all_cars.append(new_car)


    def moving_cars(self):
            for car in self.all_cars:
                car.forward(self.move_distance)
    def level_up(self):
        self.move_distance *= 1.5
        self.level += 1
