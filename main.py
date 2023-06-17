from scoreboard import Scoreboard
from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
import random
import turtle
import time


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


ball = Ball()
scoreboard = Scoreboard()
screen = Screen()
paddle = Paddle()

# Creating the screen
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Cedric's Breakout Game")
screen.tracer(0)

# Creating the paddle
screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

# Creating multicolor bullets
turtle.colormode(255)
x_cor = [
    [-260, -220, -180, -140, -100, -60, -20, 20, 60, 100, 140, 180, 220, 260],
    [-240, -200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200, 240],
    [-220, -180, -140, -100, -60, -20, 20, 60, 100, 140, 180, 220],
    [-200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200],
    [-160, -120, -80, -40, 0, 40, 80, 120, 160],
    [-140, -100, -60, -20, 20, 60, 100, 140],
    [-120, -80, -40, 0, 40, 80, 120],
    [-100, -60, -20, 20, 60, 100],
    [-60, -20, 20, 60],
    [-40, 0, 40],
    [-20, 20],
    [0]
]

y_cor = [250, 210, 170, 130, 90, 50, 10, -30, -70, -110, -150, -190]

bullets = []
range_nbr = 15
cor_nbr = -1

for _ in range(12):
    range_nbr -= 1
    cor_nbr += 1
    if range_nbr == 10:
        range_nbr = 9
    if range_nbr == 5:
        range_nbr = 4

    for index in range(range_nbr):
        bullet = Turtle()
        bullet.shape("circle")
        bullet.shapesize(stretch_wid=2, stretch_len=2)
        bullet.color("white")
        bullet.penup()
        bullet.speed("fastest")
        bullet.color(random_color())
        bullet.goto(x_cor[cor_nbr][index], y_cor[cor_nbr])
        bullets.append(bullet)

# Game ON
game_on = True
while game_on:
    time.sleep(ball.speed_up)
    screen.update()
    ball.move()

    # Bouncing
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.x_bounce()

    elif ball.ycor() > 280:
        ball.y_bounce()

    # Collusion with the paddle
    if ball.distance(paddle) < 35 and ball.ycor() < -20:
        ball.y_bounce()

    # Detecting paddle misses
    if ball.ycor() <= -300:
        ball.game_over()
        paddle.game_over()
        scoreboard.game_over()
        for bullet in bullets:
            bullet.goto(2000, 2000)

    # Collusion with bullets
    for bullet in bullets:
        if ball.distance(bullet) <= 30:
            ball.y_bounce()
            bullet.goto(1000, 1000)
            bullets.remove(bullet)
            scoreboard.point()

    # No more bullet
    if not bullets:
        scoreboard.game_over()
        ball.game_over()
        paddle.game_over()
        for bullet in bullets:
            bullet.goto(2000, 2000)

screen.exitonclick()

# # # # # TO BE ADDED LATER # # # # #
# Speed increase after collusion with paddle
# Play Again button
# Time feedback at the end
