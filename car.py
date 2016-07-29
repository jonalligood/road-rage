import numpy as np
import random

class Car:
    def __init__(self, position, car_in_front=None):
        self.acceleration = 2  # 2 m/s^2
        self.decel_chance = 0.1
        self.max_velocity = 33.3  # m/s
        self.velocity = 0
        self.position = np.array([position, position + 5])

    def update_car(self, car_in_front, road):
        if random.random() < self.decel_chance:
            self.decelerate(car_in_front)
        else:
            self.accelerate(car_in_front)
        self.get_current_position(road)

    def accelerate(self, car_in_front):
        self.velocity += self.acceleration
        if self.velocity >= self.max_velocity:
            self.velocity = self.max_velocity
        self.check_distance_between_cars(car_in_front)

    def decelerate(self, car_in_front):
        self.velocity -= self.acceleration
        self.check_distance_between_cars(car_in_front)

    def check_distance_between_cars(self, car_in_front):
        distance_between = car_in_front.position[0] - self.position[1]
        if  distance_between <= self.velocity:
            if self.velocity > car_in_front.velocity:
               self.velocity = car_in_front.velocity

    def get_current_position(self, road):
        self.position += self.velocity
        if self.position[1] >= road.length:
            self.position = self.position % road.length
