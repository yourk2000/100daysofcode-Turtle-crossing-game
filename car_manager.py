import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.move_speed = STARTING_MOVE_DISTANCE
        new_x = random.randint(-300, 300)
        while -100 < new_x < 100:
            new_x = random.randint(-300, 300)
        new_y = random.randint(-280, 280)
        self.goto(new_x, new_y)


# TODO 2: generate car randomly
class CarManager:

    def __init__(self):
        self.cars = []
        for num in range(35):
            new_car = Car()
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.forward(car.move_speed)
            if car.xcor() < -320:
                new_y = random.randint(-280, 280)
                car.goto(300, new_y)

    def increase_speed(self):
        for car in self.cars:
            car.move_speed += MOVE_INCREMENT

    def refresh(self):
        for car in self.cars:
            new_x = random.randint(-300, 300)
            while -100 < new_x < 100:
                new_x = random.randint(-300, 300)
            new_y = random.randint(-280, 280)
            car.goto(new_x, new_y)
