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
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

move_rate = 0.1
game_is_on = True
while game_is_on:
    scoreboard.update_scoreboard()
    time.sleep(move_rate)
    screen.update()
    car_manager.new_car()
    car_manager.move_cars()
    if player.ycor() > 295:
        player.next_level(move_rate)
        car_manager.level_up()
        scoreboard.increase_score()
    for vehicle in car_manager.all_cars:
        if vehicle.distance(player) < 25:
            print("Crash")
            scoreboard.game_over()
            game_is_on = False
screen.exitonclick()