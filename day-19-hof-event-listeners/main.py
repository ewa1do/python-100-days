# from turtle import Turtle, Screen
#
# tim = Turtle()
#
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_right():
#     tim.right(10)
#
# def turn_left():
#     # tim.left(15)
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# # screen.onkey(move_forwards, "Up")
# screen.onkeypress(key="w", fun=move_forwards)
# screen.onkeypress(key="s", fun=move_backwards)
# screen.onkeypress(key="d", fun=turn_right)
# screen.onkeypress(key="a", fun=turn_left)
# screen.onkeypress(key="c", fun=clear)
#
# screen.listen()
# screen.exitonclick()
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
is_race_on = False

# print(user_bet)

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230, y=-100)

for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtles.append(turtle)
    # turtle_color.goto(x=-230, y=-100)


i = 0
for turtle in turtles:
    turtle.penup()
    turtle.goto(x=-230, y=-100 - i)
    i -= 50

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
