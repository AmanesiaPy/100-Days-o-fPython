import turtle
from turtle import Turtle
import random


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        turtle.colormode(255)
        self.cars_list = []
        self.car_speed = 10

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.setheading(180)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        random_position = (300, (random.randint(-220, 220)))
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color = (r, g, b)
        car.goto(random_position)
        car.color(random_color)
        self.cars_list.append(car)

    def move_cars(self):
        for cars in self.cars_list:
            cars.forward(self.car_speed)

    def reset_car(self):
        self.car_speed += 5
