from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []

    def new_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(COLORS[random.randint(0, 5)])
        new_car.penup()
        new_car.setheading(180)
        new_car.goto(290, (random.randint(-11, 12) * 20))
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)