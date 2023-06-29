

class Vehicle:
    def __init__(self, name, max_speed, mileage) -> None:
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def print_curr_speed(self):
        print("the speed is ", self.max_speed)

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage) -> None:
        super().__init__(name, max_speed, mileage)
        self.name = "Bus " + name
    

car1 = Vehicle("Toyota", 50, 100)

bus1 = Bus("Honda", 10, 10)

print(bus1.name)
print(bus1.max_speed)
