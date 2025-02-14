# Importing
from operator import contains
from turtle import Turtle, Screen
from random import choice, randint

# Aliasing
# import Turtle as t

# Instantiation
kiki = Turtle()

screen = Screen()
screen.colormode(255)

# Shape and color
kiki.shape("turtle")
kiki.color("green")
# kiki.pensize(3)

# Set speed
kiki.speed("fastest")

def random_color():
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)

    rand_color = (r, g, b)

    return rand_color

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

def random_walk():
    directions = [0, 90, 180, 270]
    kiki.pensize(4)

    for _ in range(0, 200):
        kiki.forward(30)
        kiki.setheading(choice(directions))
        kiki.color(random_color())

def draw_spirograph():
    for i in range(0, 100):
        kiki.color(random_color())
        kiki.circle(100, 360)
        kiki.setheading(-i*5)


draw_spirograph()

# make_dashed_line()
# draw_shapes()
# random_walk()


screen.exitonclick()


