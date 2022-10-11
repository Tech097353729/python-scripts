import turtle
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.update_scoreboaed()

    def update_scoreboaed(self):
        output = f"Score : {self.score}"
        self.penup()
        self.color("white")
        self.hideturtle()
        # self.shape("circle")
        # self.shapesize(0.001)
        # self.write(arg=output, move=(0, 200), align="center", )
        self.goto((0, 275))
        self.write(arg=output, align="center", font=("Arial", 14, "bold"))
        # self.write((0, 150), True)

    def refresh(self):
        self.clear()
        self.score += 1
        self.update_scoreboaed()














