
from turtle import Turtle, Screen


turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(20)

def move_back():
    turtle.back(20)

def move_right():
    turtle.right(20)

def move_left():
    turtle.left(20)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)

screen.exitonclick()