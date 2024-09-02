from turtle import Turtle, Screen, turtles
import random
from cannon import Cannon
from score_board import Score
from alien_ships import AlienShip
from bunkers import Bunker
import time

screen = Screen()
screen.tracer(0)
screen.setup(1600, 800)
screen.bgcolor("black")
screen.title("Breakout")
screen.listen()

game_is_on = True

score_board = Score((300, 350), 0, "Score")
lives_board = Score((-300, 350), 3, "Lives")
lives = 3
a = 3
rows = 5
cols = 10
x_start = -700
y_start = 300
x_offset = 110
y_offset = 50
lasers = []
aliens = []
alien_lasers = []
last_shot_time = 0

alien_laser_rate = 100000

for row in range(rows):
    for col in range(cols):
        x = x_start + col * x_offset
        y = y_start - row * y_offset
        alien = AlienShip(x, y)
        aliens.append(alien)

cannon = Cannon((0, -360))


def draw_cannon():
    cannon.clear()
    cannon.turtlesize(1, 4)
    cannon.stamp()
    cannon.sety(-350)
    cannon.turtlesize(1, 1.5)
    cannon.stamp()
    cannon.sety(-340)
    cannon.turtlesize(0.8, 0.3)
    cannon.stamp()
    cannon.sety(-360)
    screen.update()


draw_cannon()


def move_left():
    new_x = cannon.xcor() - 40
    if new_x >= -770:
        cannon.setx(new_x)
        draw_cannon()


def move_right():
    new_x = cannon.xcor() + 40
    if new_x <= 770:
        cannon.setx(new_x)
        draw_cannon()


LASER_LENGTH = 1
LASER_SPEED = 10
COOLDOWN_TIME = 1


def create_laser():
    global last_shot_time
    current_time = time.time()

    if current_time - last_shot_time >= COOLDOWN_TIME:
        laser = Turtle()
        laser.penup()
        laser.color(1, 0, 0)
        laser.hideturtle()
        laser.setposition(cannon.xcor(), cannon.ycor())
        laser.setheading(90)
        laser.pendown()
        laser.pensize(5)
        lasers.append(laser)
        laser.showturtle()
        last_shot_time = current_time


def move_laser(laser):
    laser.clear()
    laser.forward(LASER_SPEED)
    laser.forward(LASER_LENGTH)
    laser.forward(-LASER_LENGTH)


def create_alien_laser():
    for alien in aliens:
        random_chance = random.randint(1, alien_laser_rate)
        if random_chance == 1:
            alien_laser = Turtle()
            alien_laser.penup()
            alien_laser.color(0, 1, 0)
            alien_laser.hideturtle()
            alien_laser.setposition(alien.x, alien.y)
            alien_laser.setheading(-90)
            alien_laser.pendown()
            alien_laser.pensize(2)
            alien_lasers.append(alien_laser)
            alien_laser.showturtle()


def move_alien_laser(alien_laser):
    alien_laser.clear()
    alien_laser.forward(0.1)
    alien_laser.forward(LASER_LENGTH)
    alien_laser.forward(-LASER_LENGTH)


screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(create_laser, "space")


bunkers = []

for a in range(1, 4):
    for y in range(0, 5):
        for x in range(0, 10):
            bunker = Bunker(-900 + x*21 + a*400, -200 + y*20)
            bunkers.append(bunker)


while game_is_on:
    screen.update()
    change_direction = False
    for laser in lasers[:]:
        move_laser(laser)
        if laser.ycor() > 400:
            laser.clear()
            laser.hideturtle()
            lasers.remove(laser)

        else:
            for alien in aliens[:]:
                if laser.distance(alien.alien) < 20:
                    laser.clear()
                    laser.hideturtle()
                    lasers.remove(laser)
                    alien.destroy()
                    aliens.remove(alien)
                    score_board.increase_score(10)
                    break
            for bunker in bunkers[:]:
                if laser.distance(bunker.bunker) < 20:
                    laser.clear()
                    laser.hideturtle()
                    lasers.remove(laser)
                    bunker.destroy()
                    bunkers.remove(bunker)
                    break

    for alien in aliens:
        create_alien_laser()
        for alien_laser in alien_lasers[:]:
            move_alien_laser(alien_laser)
            for bunker in bunkers:
                if alien_laser.distance(bunker.bunker) < 20:
                    alien_laser.clear()
                    alien_laser.hideturtle()
                    alien_lasers.remove(alien_laser)
                    bunker.destroy()
                    bunkers.remove(bunker)
                    break
            if alien_laser.distance(cannon) < 20:
                alien_laser.clear()
                alien_laser.hideturtle()
                alien_lasers.remove(alien_laser)
                lives -= 1
                lives_board.increase_score(-1)
                if lives == 0:
                    score_board.game_over()
                    game_is_on = False
        if alien.x > 770 or alien.x < -770:
            change_direction = True
            break

        if alien.y < -360:
            score_board.game_over()
            game_is_on = False

    if change_direction:
        a *= -1
        alien_laser_rate = int(alien_laser_rate * 0.8)
        print(alien_laser_rate)
        if alien_laser_rate < 10000:
            alien_laser_rate = 10000
        if a > 0:
            a += 1
        else:
            a -= 1
        for alien in aliens:
            alien.move(0, -10)

    for alien in aliens:
        alien.move(a, 0)
        time.sleep(0.001)

    if not aliens:
        score_board.win_game()
        game_is_on = False


screen.exitonclick()
