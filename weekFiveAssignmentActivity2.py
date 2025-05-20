# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Car class
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

# Plane class
class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

# Boat class
class Boat(Vehicle):
    def move(self):
        print("Sailing on the water 🚤")

# Bicycle class
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the path 🚲")

# Polymorphism in action
def vehicle_move_test(vehicle):
    vehicle.move()

# Create a list of different vehicles
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Test each vehicle's move method
print("🌍 Vehicle Movements:\n")
for v in vehicles:
    vehicle_move_test(v)
