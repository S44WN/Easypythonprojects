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
tim.pensize(15)

directions = [0, 90, 180, 270]

tim.speed("fastest")

for _ in range(20000):
    tim.color(random.choice(COLORS))
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen.exitonclick()
