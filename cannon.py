from turtle import Turtle


class Cannon(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.setpos(position)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())


