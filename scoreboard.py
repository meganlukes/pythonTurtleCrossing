from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(-220, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
