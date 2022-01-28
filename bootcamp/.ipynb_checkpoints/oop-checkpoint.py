#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        

        
Big_yellow = Bus(Big_yellow, 55, 9000)

#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

#result:
Vehicle Name: School Volvo Speed: 180 Mileage: 12

            
#4 Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

    
#     OOP Exercise 5: Define a property that must have the same value for every class instance (object)
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

class Vehicle:
    
    
    Vehicle.color = 'white'

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


# OOP Exercise 6: Class Inheritance
# Given:

# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

# Note: The bus seating capacity is 50. so the final fare amount should be 5500. 
#You need to override the fare() method of a Vehicle class in Bus class.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100
#Bus instance:  add an extra 10% on full fare as a maintenance charge. 
#for bus instance : total fare = total fare + 10% of the total fare.

class Bus(Vehicle):
    def fare(self):
        return (Vehicle.seating_capacity*100)*.1
    pass

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

# OOP Exercise 7: Check type of an object
# Write a program to determine which class a given Bus object belongs to.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

#instance.__class__.__name__

School_bus.__class__.__name__
>>>'Bus'

print(type(School_bus))
>>><class '__main__.Bus'>

OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class