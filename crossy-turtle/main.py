import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
screen.listen()
screen.onkeypress(player.go_up, "Up")

scoreboard = Scoreboard()
speed_up = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1*speed_up)
    screen.update()
    car_manager.generate_car()
    car_manager.move_cars()
    car_manager.car_off_the_screen()

    for car in car_manager.all_cars:
        if player.distance(car) <20:
            game_is_on = False
            scoreboard.game_over()

    #detecting finished level
    if player.check_finish():
        player.go_to_start()
        # car_manager.level_up()
        scoreboard.increase_level()
        speed_up *= 0.7




screen.exitonclick()