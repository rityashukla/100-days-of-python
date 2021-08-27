from turtle import Turtle,Screen
from snake_game import Snake
from food import Food
from score_board import Score
import time
screen=Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")



# segment2=Turtle("square")
# segment2.color("white")
# segment2.goto(-20,0)
# segment2=Turtle("square")
# segment2.color("white")
# segment2.goto(-40,0)
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    #detect collision
    if snake.head.distance(food)<15:
        food.refresh()
        score.increase_score()
        snake.increase_snake()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.xcor()>280 or snake.head.ycor()<-280:
        game_on=False
        score.game_over()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_on=False
            score.game_over()


        


    
        





screen.exitonclick()
