from turtle import Turtle, Screen
import random
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

# def front_collision():
#     if character.xcor() <= car.xcor() and character.ycor() - car.ycor() < 20:
#         if character.ycor() > car.ycor():
#             if character.distance(car) <= 34:
#                 print("collision2")
#         elif character.distance(car) <= 30:
#             print('collision1')
#         elif character.ycor() <= car.ycor() and character.ycor() - car.ycor() >= -10:
#             if character.distance(car) <= 34:
#                 print("collision3")
#     if car.xcor() <= character.xcor() <= car.xcor() + 30:
#         if character.ycor() < car.ycor() and character.ycor() - car.ycor() >= -20 :
#             if character.distance(car) <= 30:
#                 print("collision4")
#         if character.ycor() > car.ycor():
#             if character.ycor() - car.ycor() >= 20:
#                 pass
#             elif character.distance(car) <=23:
#                     print("collision5")



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






# def move():
#     turtle.forward(10)
#
# alive = True
# game_speed = 0.25
# x= 2
# y=6
# create_cars()
# while alive:
#
#     screen.update()
#     time.sleep(0.1)
#
#     screen.onkeypress(move,'Up')
#
#     for i in cars:
#         speed = random.randint(x,y)
#         i.forward(speed)
#         if i.xcor() < -310:
#             i.setx(300)
#         if i.distance(turtle) <= 27:
#             screen.update()
#             alive = False
#     if turtle.ycor() > 230:
#         for car in cars:
#             car.goto(random.randint(-250, 280),random.randint(-180, 220))
#
#         turtle.sety(-250)
#         x += 3
#         y+=3
#         speed = random.randint(x,y)
#
#
#     screen.listen()
#


screen.exitonclick()