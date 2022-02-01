# Exercise 41. 

# 1.Write a Rectangle class in Python language, 
# allowing you to build a rectangle with length and width attributes.

# 2.Create a Perimeter() method to calculate the perimeter 
# of the rectangle and a Area() method to calculate the area of ​​the rectangle.

# 3.Create a method display() that display the length, width, perimeter and area of an 
# object created using an instantiation on rectangle class.


# 4.Parallelepipede:In geometry, a parallelepiped is a three-dimensional figure formed by six parallelograms. 
# By analogy, it relates to a parallelogram just as a cube relates to a square.
# Create a Parallelepipede child class inheriting from the Rectangle  
# class and with a height attribute and another Volume() 
# method to calculate the volume of the Parallelepiped.

class Rectangle:
    def __init__(self, length,width):
        self.length = length
        self.width = width
    
    def perimeter(self):
        print('The perimeter of the rectangle is', (2*(self.length+self.width)))
        return 2*(self.length+self.width)
    
    def area(self):
        print('The area of the rectangle is', (self.length*self.width))
        return (self.length*self.width)
    
    def display(self):
        print('The width of the rectangle is', self.width)
        print('The length of the rectangle is', self.length)
        print('The perimeter of the rectangle is', self.perimeter())
        print('The areea of the rectangle is', self.area())
        
        def display(self):
        print("The length of rectangle is: ", self.length)
        print("The width of rectangle is: ", self.width)
        print("The perimeter of rectangle is: ", self.perimeter())
        print("The area of rectangle is: ", self.area())
 m = Rectangle(10,2)
print(m.perimeter())
print(m.area())

The perimeter of the rectangle is 24
24
The area of the rectangle is 20
20
class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(length, width)
        self.height = height
        
    def volume(self):
        return (self.length*self.width*self.height)


class Parallelepipede(Rectangle):
    def __init__(self, length, width , height):
        Rectangle.__init__(self, length, width)
        self.height = height