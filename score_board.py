from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 30, 'normal')


class Score(Turtle):
    def __init__(self, position, score, name):
        super().__init__()
        self.goto(position)
        self.color("white")
        self.hideturtle()
        self.score = score
        self.update_score(name)
        self.name = name

    def update_score(self, name):
        self.write(f"{name}: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, increase):
        self.score += increase
        self.clear()
        self.update_score(self.name)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def win_game(self):
        self.goto(300, 0)
        self.write("You won !", align=ALIGNMENT, font=FONT)
