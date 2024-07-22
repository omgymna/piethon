FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-280,270)
        self.write(f"Level: {self.level}", align= "left", font = FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()


    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over, Final Score: {self.level}", align= "center", font = FONT)

