from turtle import Turtle

DIRECTION = 90
class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(DIRECTION)
        self.steps = 10

    def move(self):
        self.forward(self.steps)

    def front_collision(self, car):
        if self.xcor() <= car.xcor() and self.ycor() - car.ycor() < 20:
            if self.ycor() > car.ycor():
                if self.distance(car) <= 34:
                    return True
            elif self.distance(car) <= 30:
                return True
            elif self.ycor() <= car.ycor() and self.ycor() - car.ycor() >= -10:
                if self.distance(car) <= 34:
                    return True
    def run_into_car_collision(self,car):
        if car.xcor() <= self.xcor() <= car.xcor() + 30:
            if self.ycor() < car.ycor() and self.ycor() - car.ycor() >= -20:
                if self.distance(car) <= 30:
                    return True
            if self.ycor() > car.ycor():
                if self.ycor() - car.ycor() >= 20:
                    pass
                elif self.distance(car) <= 23:
                    return True

