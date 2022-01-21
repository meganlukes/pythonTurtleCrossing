from turtle import Turtle
import random
COLORS = ["dodger blue", "magenta", "blue violet", "dark orchid", "deep pink", "deep sky blue"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(COLORS[random.randint(0, 5)])
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(290, (random.randint(-11, 12) * 20))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT