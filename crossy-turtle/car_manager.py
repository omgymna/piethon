COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2,stretch_wid = 1)
            new_car.penup()
            new_car.color(random.choice(COLORS))

            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)

            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def car_off_the_screen(self):
        for car in self.all_cars:
            if car.xcor() < -350:
                car.hideturtle()
                self.all_cars.remove(car) 
                