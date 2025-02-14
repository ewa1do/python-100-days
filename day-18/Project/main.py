# import colorgram
import turtle as t
import random

kiki = t.Turtle()

screen = t.Screen()
screen.colormode(255)

kiki.penup()
kiki.hideturtle()
kiki.shape("classic")

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     new_color = (r, g, b)
#
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(120, 166, 185), (159, 14, 21), (34, 110, 157), (232, 82, 46), (124, 176, 144), (8, 97, 38), (171, 21, 16), (199, 65, 28), (185, 186, 27), (31, 128, 47), (12, 41, 74), (15, 63, 40), (242, 202, 5), (138, 82, 95), (85, 15, 22), (51, 166, 77), (44, 26, 22), (6, 65, 137), (173, 135, 149), (232, 170, 160), (48, 150, 195), (219, 66, 71), (74, 135, 186), (169, 206, 175)]

for i in range(1, 11):
    for j in range(0, 10):
        kiki.dot(20, random.choice(color_list))
        kiki.forward(50)

    kiki.teleport(0, i * 40)


screen.exitonclick()


