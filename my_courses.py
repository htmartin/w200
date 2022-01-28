# Exercise 41. Rectangle class: ||  Solution
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
    