from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-200, 250)
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="Center", font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align="center", font=FONT)
