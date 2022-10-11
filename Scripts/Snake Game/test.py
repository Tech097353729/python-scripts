import turtle
from turtle import Screen , Turtle
import time



screen = Screen()
screen.bgcolor("black")
screen.setup(width=600 , height=600)
screen.title("My Snake Game")
screen.tracer(0) # turn off the animation on screen


INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]
SEGMENT_SQUARE = []
SQUARE_SIZE = 20

def create_snake():
    """"It will create an initial snake structure."""
    for pos in INITIAL_POSITION:
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(pos)
        SEGMENT_SQUARE.append(segment)
        # time.sleep(1)
    screen.update()



create_snake()
game_is_on = True
# time.sleep(5)
# time.sleep(2)
def up():
    SEGMENT_SQUARE[0].left(90)


screen.listen()
screen.onkey(up,"Up")
# screen.onkey(down,"Down")


while game_is_on:
    screen.tracer(0)

    for seg in range(len(SEGMENT_SQUARE)-1,0,-1):
        x_cor = SEGMENT_SQUARE[seg-1].xcor()
        y_cor = SEGMENT_SQUARE[seg-1].ycor()
        SEGMENT_SQUARE[seg].goto(x_cor,y_cor)
    SEGMENT_SQUARE[0].fd(20)
    # SEGMENT_SQUARE[0].left(90)

    screen.update()
    time.sleep(0.1)




screen.exitonclick()