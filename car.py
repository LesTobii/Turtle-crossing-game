from turtle import Turtle
import random

DIRECTION = 180
COLORS = ['red','orange','blue','yellow','green','indigo','violet']


class Car(Turtle):
    def __init__(self):
        super().__init__()
        # self.cars= []
        self.speed_lower_limit = 2
        self.speed_higher_limit = 5
        self.generate_car()

    def generate_car(self):
        self.shape("square")
        self.penup()
        self.setheading(DIRECTION)
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        y = random.randint(-160, 200)
        x = random.randint(-250, 280)
        self.goto(x, y)

    def move_car(self):
        self.forward(random.randint(self.speed_lower_limit,self.speed_higher_limit))
        # self.forward(5)
    def out_of_bounds(self):
        self.setx(280)
        self.sety(random.randint(-160,200))

