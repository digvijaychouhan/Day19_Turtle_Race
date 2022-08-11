import turtle
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(height=600, width=800)
is_race_on = False
colors = ["red", "blue", "green", "orange", "cyan", "purple"]
y_positions = [-160, -80, 0, 80, 160, 240]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-390, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? "
                                                          "(red/blue/green/orange/cyan/purple)")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 380:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")
        random_num = randint(0, 10)
        turtle.forward(random_num)

screen.exitonclick()
