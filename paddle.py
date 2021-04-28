from turtle import Turtle

UP = 90
DOWN =270

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.paddle = self.create_paddle(position)

    def create_paddle(self, position):
        piece = Turtle("square")
        piece.penup()
        piece.goto(position)
        piece.color("white")
        piece.resizemode("user")
        piece.shapesize(stretch_wid=5, stretch_len=1)
        return piece

    def up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)


