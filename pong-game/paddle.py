
from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,starting_position):
        super().__init__()
        self.shape('square')
        self.shapesize(5,1)
        self.color('white')
        self.penup()
        self.goto(starting_position[0],starting_position[1])

    def go_up(self):
        if self.ycor() <= 250:
            new_y = self.ycor()+30
            self.goto(self.xcor(),new_y)
    
    def go_down(self):
        if self.ycor() >= -250:
            new_y = self.ycor()-30
            self.goto(self.xcor(),new_y)
