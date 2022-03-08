from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-75, -45, -15, 15, 45, 75]
is_race_on = False
all_turtle = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            turtle_color = turtle.pencolor()
            is_race_on = False
            if user_bet == turtle_color:
                print(f"You win!. The wining turtle is {turtle_color}.")
            else:
                print(f"You lose!. The wining turtle is {turtle_color}.")
        rand_speed = random.randint(0, 10)
        turtle.forward(rand_speed)


screen.exitonclick()
