from turtle import Turtle

UP = 90
DOWN =270

class Paddle:

    def __init__(self):
        self.paddle = self.create_paddle()


    def create_paddle(self):
        piece = Turtle("square")
        piece.color("white")
        piece.resizemode("user")
        piece.shapesize(stretch_wid=5, stretch_len=1)
        piece.penup()
        piece.goto(x=350, y=0)
        return piece

    def up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)


