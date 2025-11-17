from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')

paddle = Paddle()

screen.setup(width=800, height=600)
screen.title('Pong')


screen.exitonclick()