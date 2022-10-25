import random
from turtle import Turtle, Screen
screen = Screen()
screen.bgcolor("grey81")

COLORS = ['antiquewhite1', 'aquamarine1', 'azure1',
          'aqua', 'azure4', 'darkseagreen1', 'deepskyblue4', 'floralwhite', 'honeydew2', 'khaki1',
          'lavenderblush1', 'lightblue2', 'lightcoral', 'lightpink1', 'lightseagreen',
          'lightslateblue', 'linen', 'mediumpurple1', 'mediumspringgreen', 'palegreen1', 'paleturquoise1',
          'palevioletred2', 'pink2', 'powderblue', 'red1', 'rosybrown1', 'seagreen1',
          'red', 'thistle1', 'turquoise']

tim = Turtle()
tim.shape('turtle')
tim.pensize(2)
tim.penup()
tim.backward(50)
tim.left(90)
tim.forward(300)
tim.right(90)
tim.pendown()

sides = 3

while sides < 25:
    angle = 360/sides
    for i in range(sides):
        tim.forward(100)
        tim.right(angle)
    tim.pencolor(random.choice(COLORS))
    tim.color(random.choice(COLORS))

    sides += 1


screen.exitonclick()
