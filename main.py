import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

sleep_time = 0.1
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    car_manager.move_car()
    # TODO 3: detect collision with car
    # for car in car_manager.cars:
    #     if player.distance(car) < 22:
    #         game_is_on = False
    #         scoreboard.game_over()

    # TODO 5: level up when reach the end
    if player.ycor() > 280:
        player.start()
        scoreboard.level += 1
        sleep_time *= 0.5
        scoreboard.update()
        car_manager.refresh()
# TODO 4: make scoreboard

screen.exitonclick()
