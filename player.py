from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.color("white")

    def up(self):
        self.forward(MOVE_DISTANCE)

    def next_level(self, move_rate):

        self.goto(STARTING_POSITION)
        move_rate *= 0.5