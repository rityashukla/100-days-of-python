from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        # self.r_paddle()
        # self.l_paddle()
        #self.goto(350,0)
    
    def r_paddle(self):
        self.goto(350,0)

    def l_paddle(self):
        self.goto(-350,0)
        
    def go_up(self):
        #self.r_paddle()
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)
    def go_down(self):
        #self.r_paddle()
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)
    
    