import turtle


from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape('turtle')
jimmy.color('aquamarine')

for steps in range(4):
    jimmy.forward(100)
    jimmy.right(90)


screen = Screen()
screen.exitonclick()
