from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        if self.ycor() <= 300:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def check_finish(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return 
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)