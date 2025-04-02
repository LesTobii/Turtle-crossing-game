from turtle import Screen
import time
from car import Car
from character import Character
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width = 600, height = 600)
screen.colormode(255)
screen.tracer(0)

character = Character()
character.goto(0,-250)
scoreboard = Scoreboard()

cars = []
for i in range(25):
    cars.append(Car())

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)

    screen.onkeypress(character.move, "Up")
    screen.listen()
    for car in cars:
        car.move_car()
        if car.xcor() < -300:
           car.out_of_bounds()

        if character.front_collision(car) or character.run_into_car_collision(car):
            screen.update()
            game_over = True

        if character.ycor() > 250:
            character.sety(-250)
            scoreboard.update_scoreboard()
            #increase the speed of the car at this point of the loop to go
            #faster than the others, to make the game more challenging
            car.speed_lower_limit += 6
            car.speed_higher_limit += 6

            for i in cars:
                i.speed_lower_limit += 2
                i.speed_higher_limit += 2


screen.exitonclick()