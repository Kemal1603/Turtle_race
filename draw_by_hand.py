import turtle
import random

kemal = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
colors = [(255, 0, 0), (3, 0, 0), (253, 161, 187), (0, 66, 254), (0, 246, 0), (223, 217, 103)]
kemal.pen(pensize=10)


def move_forwards():
    kemal.color(random.choice(colors))
    kemal.forward(20)


def move_backwards():
    kemal.backward(10)


def move_left():
    kemal.left(10)


def move_right():
    kemal.right(10)


def clear():
    kemal.clear()
    kemal.penup()
    kemal.home()
    kemal.pendown()


screen.listen()
screen.onkey(fun=move_forwards, key='Up')
screen.onkey(fun=move_backwards, key='Down')
screen.onkey(fun=move_left, key='Left')
screen.onkey(fun=move_right, key='Right')
screen.onkey(fun=clear, key='c')
screen.exitonclick()





