from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")

paddle = Paddle()
screen.listen()
screen.onkey(fun=paddle.up, key="Up")
screen.onkey(fun=paddle.down, key="Down")



screen.exitonclick()