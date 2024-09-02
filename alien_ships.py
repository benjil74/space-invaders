from turtle import Turtle


class AlienShip:
    def __init__(self, x, y, color="green"):
        self.x = x
        self.y = y
        self.size = 20
        self.health = 20
        self.shape = "triangle"
        self.color = color
        self.move_speed = 0.05
        self.alien = Turtle()
        self.alien.shape(self.shape)
        self.alien.color(self.color)
        self.alien.penup()
        self.alien.goto(self.x, self.y)
        self.alien.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.alien.setheading(270)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.alien.goto(self.x, self.y)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.destroy()

    def destroy(self):
        self.alien.hideturtle()

