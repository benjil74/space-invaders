from turtle import Turtle


class Bunker:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.shape = "square"
        self.color = "green"
        self.bunker = Turtle()
        self.bunker.shape(self.shape)
        self.bunker.color(self.color)
        self.bunker.penup()
        self.bunker.goto(self.x, self.y)
        self.bunker.shapesize(stretch_wid=2, stretch_len=2)

    def destroy(self):
        self.bunker.hideturtle()

