from ball import Ball
from paddle import Paddle
from turtle import Screen
import time

GAME_SPEED = 0.08

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "W".lower())
screen.onkey(l_paddle.go_down, "S".lower())
game_is_on = True

while game_is_on:
    time.sleep(GAME_SPEED)
    screen.update()
    ball.move()


screen.exitonclick()
