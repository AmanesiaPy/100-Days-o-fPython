from turtle import Screen
from player import Player
from car import Cars
from score_board import ScoreBoard
import random
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = Cars()
score_board = ScoreBoard()

screen.listen()
screen.onkey(player.move_up, "Up")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    score_board.show_score()
    to_create_car = random.randint(0, 3)
    if to_create_car == 1:
        cars.create_car()
    cars.move_cars()

    # Detect car hit
    for car in cars.cars_list:
        if player.distance(car) < 23:
            is_game_on = False
            score_board.game_over()

    # Detect turtle move up
    if player.ycor() > 280:
        player.reset_player()
        cars.reset_car()
        score_board.next_level()

screen.exitonclick()
