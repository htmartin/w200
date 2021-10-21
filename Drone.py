class Drone:
    '''rep of a drone aircraft'''
    power_system ='battery'
    def fly(self):
        return 'The ' + self.power_system + '-powered drone is flying.'
    
    
    
d1 = Drone()
d2 = Drone()

d1.powersystem = 'dream'

print(d1.fly())
print(d2.fly())
#_______________________________________________________________________

class Drone:
    '''rep of a drone aircraft'''
    power_system ='battery'
    def fly(self):
        print ('The ' + self.power_system + '-powered drone is flyingat an altitude of '+ str(self.altitude))
    
    def ascend(self, change):
        self.altitude += change
        
d = Drone()
d.altitude = 0
d.fly()
d.ascend(100)
d.fly()

#_______________________________________________________________________7.8
class Drone:
    '''rep of a drone aircraft'''
    
    power_system ='battery'
    
    def __init__(self,altitude=0):
         self.altitude = altitude
    
    def fly(self):
        print ('The ' + self.power_system + '-powered drone is flying at an altitude of '+ str(self.altitude))
    
    def ascend(self, change):
        self.altitude += change
        
d = Drone(100)
d.fly()
d.ascend(100)
d.fly()
d2 = Drone()

#________________________________________________________________
#Counting with data attributes:instance attributes
class Drone:
    '''rep of a drone aircraft'''
    
    power_system ='battery'
    
    def __init__(self,altitude=0):
        self.altitude = altitude
        self.ascend_count = 0
    
    def fly(self):
        print ('The ' + self.power_system + '-powered drone is flying at an altitude of '+ str(self.altitude))
    
    def ascend(self, change):
        self.altitude += change
        self.ascend_count += 1
        
d = Drone(100)
print('d ascend count is',d.ascend_count)
d.fly()
d.ascend(100)
d.ascend(100)
print('d ascend count is',d.ascend_count)
d.fly()
d2 = Drone()
print('d2 ascend count is',d2.ascend_count)

#________________________________________________________________
#Counting with data attributes 2: Class attributes
class Drone:
    '''rep of a drone aircraft'''
    num_drones =0
    power_system ='battery'
    
    def __init__(self,altitude=0):
        self.altitude = altitude
        self.ascend_count = 0
        num_drones +=1
    
    def fly(self):
        print ('The ' + self.power_system + '-powered drone is flying at an altitude of '+ str(self.altitude))
    
    def ascend(self, change):
        self.altitude += change
        self.ascend_count += 1
        
d = Drone(100)
d.fly()
d2 = Drone()
print('There are',Drone.num_drones, 'drones')