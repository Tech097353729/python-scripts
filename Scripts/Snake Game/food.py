import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.create_food()

    def create_food(self):
        self.shape("circle")
        self.color("blue")
        self.penup()
        [cor_x, cor_y] = self.random_cordinate_generate()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.goto(cor_x, cor_y)
        self.speed("fastest")

    def random_cordinate_generate(self):
        cor_x = random.randint(-280, 280)
        cor_y = random.randint(-280, 280)
        return [cor_x,cor_y]

    def update_food(self):
        [cor_x, cor_y] = self.random_cordinate_generate()
        self.goto(cor_x, cor_y)