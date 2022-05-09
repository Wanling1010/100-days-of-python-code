# import colorgram
# # Extract 6 colors from an image.
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

import turtle as t
import random
tim = t.Turtle()
tim.penup()
tim.speed("fastest")
t.colormode(255)
color_list = [(243, 225, 74), (179, 78, 29), (49, 36, 26), (219, 151, 76), (146, 28, 41), (22, 25, 69), (44, 43, 120), (243, 236, 239), (170, 21, 16), (48, 87, 158), (210, 85, 128), (156, 50, 86), (120, 160, 224), (27, 43, 28), (215, 79, 62), (139, 183, 140), (115, 106, 202), (75, 120, 57), (65, 30, 35), (157, 179, 231), (150, 211, 191), (204, 135, 43), (86, 87, 33), (87, 155, 109), (202, 121, 162), (61, 148, 170), (55, 100, 18)]
"""change the pointer to south-west"""
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    """size is 20 and interval is 50"""
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen = t.Screen()
screen.exitonclick()

