# Importing
from operator import contains
from turtle import Turtle, Screen
from random import choice

# Aliasing
# import Turtle as t

# Instantiation
kiki = Turtle()

# Shape and color
kiki.shape("turtle")
kiki.color("green")
kiki.pensize(3)

# Set speed
kiki.speed(10)


def draw_square():
    # Motion
    kiki.forward(100)
    kiki.right(90)
    kiki.forward(100)
    kiki.right(90)
    kiki.forward(100)
    kiki.right(90)
    kiki.forward(100)

def make_dashed_line(distance=50):
    for i in range(0, distance):
        kiki.forward(5)
        kiki.penup()
        kiki.forward(5)
        kiki.pendown()

def draw_shapes(num_shapes=10):
    kiki.teleport(0, 300)
    grades = 360

    color_list = [
        "black",
        "blue",
        "navy",
        "deep sky blue",
        "light sea green",
        "gray",
        "gold",
        "tomato",
        "purple",
        "indigo",
    ]

    def draw_trace(angle):
        kiki.forward(100)
        kiki.right(angle)

    def draw_shape(num_sides, angle):
        for _ in range(0, num_sides):
            draw_trace(angle)


    for i in range(3, num_shapes+1):
        kiki.color(choice(color_list))
        draw_shape(num_sides=i, angle=grades/i)

# def make_random_walk():
#     print("hello")
#     kiki.forward(100)
#     kiki.circle(200)

# draw_shapes(10)
# make_random_walk()



screen = Screen()
screen.exitonclick()


