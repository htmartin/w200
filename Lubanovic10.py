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
    
    
a_car = Car()

print(a_car.exclaim())

#Getters and Setters_________________________________________


class Duck :
    def __init__ ( self , input_name ):
        self . hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self . hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

don= Duck('Donald')
don.get_name()

 
>>> don = Duck ( 'Donald' ) >>> don . get_name () inside the getter 'Donald' >>> don . set_name ( 'Donna' ) inside the setter >>> don . get_name () inside the getter 'Donna'


################Property attributes________________________________________________________________________
class Duck :
    def __init__ ( self , input_name ):
        self . hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self . hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
        #name = property(get_name, set_name)
        
        
don= Duck('Donald')
#don.get_name()
don.name = 'Donna'
don.name