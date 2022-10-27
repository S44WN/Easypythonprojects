import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading + size_of_gap)


screen = t.Screen()
screen.exitonclick()
