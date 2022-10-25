from turtle import Turtle, Screen

jim = Turtle()
jim.shape('turtle')
jim.color('aquamarine')

for i in range(10):
    jim.forward(10)
    jim.penup()
    jim.forward(5)
    jim.pendown()


screen = Screen()
screen.exitonclick()
