import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
car = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

move_rate = 0.4
game_is_on = True
while game_is_on:
    time.sleep(move_rate)
    screen.update()
    car.new_car()
    car.move_cars()
    if player.ycor() > 295:
        player.next_level(move_rate)