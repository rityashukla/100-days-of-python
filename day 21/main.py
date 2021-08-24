from turtle import Turtle,Screen
from paddle import Paddle
from scoreboard import Scoreboard
import turtle
from ball import Ball
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.tracer(0)
timmy=turtle.Turtle()

ball=Ball()
r_paddle=Paddle()
l_paddle=Paddle()
r_paddle.r_paddle()
l_paddle.l_paddle()
score=Scoreboard()
timmy.goto(0,300)
while(timmy.ycor()!=-300):
    
    
    timmy.setheading(270)
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
    timmy.color("white")
    timmy.hideturtle()
screen.listen()
screen.onkey(r_paddle.go_up,"Up",)
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_on=True

while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.y_bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.x_bounce()

    if ball.xcor()>380:
        #ball.x_bounce()
        ball.reset()
        score.l_point()
        
    if ball.xcor()<-380:
        #ball.x_bounce()
        ball.reset()
        score.r_point()


screen.exitonclick()
