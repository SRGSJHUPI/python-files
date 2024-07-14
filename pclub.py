import math

class Car:
    def __init__(self, make, model, year, speed, x, y):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
        self.x = x
        self.y = y

    def accelerate(self, speed_increment):
        self.speed += speed_increment

    def brake(self, speed_decrement):
        self.speed -= speed_decrement

    def move(self):
        self.x += self.speed

    def detect_collision(self, car2):
        if abs(self.x - car2.x) < 10 and abs(self.y - car2.y) < 10:
            return True
        else:
            return False

    def time_to_collision(self, car2):
        distance_x = car2.x - self.x
        distance_y = car2.y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)
        time_to_collision = distance / (self.speed - car2.speed)
        return time_to_collision
    
car1 = Car("Hyundai", "Creta", 2022, 60, 0, 0)
car2 = Car("Maruti", "Alto", 2020, 50, 50, 50)

print(car1.make, car1.model, car1.year, car1.speed, car1.x, car1.y)
print(car2.make, car2.model, car2.year, car2.speed, car2.x, car2.y)

car1.accelerate(10)
car2.brake(20)

print(car1.speed)
print(car2.speed)

car1.move()
car2.move()

print(car1.x, car1.y)
print(car2.x, car2.y)

print(car1.detect_collision(car2))
print(car1.time_to_collision(car2))