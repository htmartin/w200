class Dog:
    """define an animal"""
    species = 'mammal'
    
    def __init__(self,color):
        self.color = color

Booboo = Dog(color= 'brown')
Bingo = Dog(color = 'white')

#______________________________________________________________

class Circle:
    """define a shape"""

    pi = 3.14
    def __init__(self,radius =1):
        self.radius = radius 
        self.area = radius * radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2
    
    def get_diameter(self):
        return self.radius*2


c = Circle()

print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())

c.setradius(2)

print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())

#_____________________________________________________________

class Animal:
    def __init__(self):
        print('Animal created')
        
    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

        
class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')
        
    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")
        
d = Dog()
#________________________________________________________

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Woof!'
    
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!' 
    
niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())