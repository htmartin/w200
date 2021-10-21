class Car():
    '''parent class'''
    def exclaim(self):
        print("I'm a car")
class Yugo(Car):
    '''subclass Car'''

    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish." )
    
    def need_a_push(self):
        print("A little help here!")
        
        
my_new_car = Car()
my_yugo = Yugo()
print(my_new_car.exclaim())
print(my_yugo.exclaim())

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_yugo.need_a_push()



#Get Help from Your Parent with super()_________________________________________

class Person ():
    def __init__ ( self , name ):
        self . name = name 

        
class EmailPerson ( Person ):
    def __init__ ( self , name , email ):
        super () . __init__ ( name )
        self . email = email 

        
bob = EmailPerson ( 'Bob Frapples' , 'bob@frapples.com' )

#Multiple Inheritance & Mixins________________________________________________

#In self Defense_________________________________________

