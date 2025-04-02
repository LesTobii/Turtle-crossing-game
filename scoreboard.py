from turtle import Turtle

POSITION = (-260, 220)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
        self.level = 1
        self.create_scoreboard()


    def create_scoreboard(self):
        self.goto(POSITION)
        self.write(arg=f'level {self.level}',font=('Papyrus', 40, 'bold'))

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.create_scoreboard()
        print('well well well')