from turtle import Turtle
import random



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.move()

    def move(self):
        RAND_X = random.randint(-280, 280)
        RAND_Y = random.randint(-280, 280)
        self.goto(RAND_X,RAND_Y)