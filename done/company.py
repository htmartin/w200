# 7.7 Make a class "company"

# Give it a docstring that describes the intent and fuction of the class
# Make two methods to add some attributes on demand: add_employee_name     add_funding
# The methods should intake self and a default value (i.e. employee_name="unnamed" or amount=0)
# For the add employee method; append the new name to the list and add one to the employee count
# For the funding amount append it to the list and increment the amount to the funding total
# Don't bother with an init() method yet



class Company():
    '''
    set up a company
    '''
    
    employee_list=[]
    employee_count=1
    funding_list=[]
    funding_amount =0
    
    #Update these methods
    def add_employee_name(self, employee_name = "unnamed"):
        Company.employee_list.append(employee_name)
        Company.employee_count +=1
    

    def add_funding(self, amount=0):
        Company.funding_amount += amount
        
        
c1 = Company()
c1.add_employee_name("Gunnar")

c2 = Company()
c2.add_funding(10000000)
c2.add_funding(50000)

#__________________________________
# 7.9
# Initializing a Class
# Add an init magic method to initialize funding and employee data as instance (rather than class) attributes.

# Require that one employee name is added at the opening of a company

# Make the initial funding amount default to 0.

# Don't forget your self arguments; instance attributes need self arguments!

# Enhance your add employee method; if the method is called without an argument and the default value (employee_name == "unnamed") is used then do not add unnamed to the list and print a message to instruct the user to add a name.


class Company():
    '''
    set up a company - add the __init__() part
    '''
    
    def __init__(self,employee_name = "unnamed", funding_amount =0):
        self.employee_list=[]
        self.employee_count=0
        self.funding_amount =0

    
    def add_employee_name(self,new_employee_name): 
        self.employee_list.append(new_employee_name)
        self.employee_count +=1
 
            
    def add_funding(self, change):
        self.funding_amount += change

c1 = Company()
c1.add_employee_name("Gunnar")
print(c1.employee_list, '= c1 employee list')
c1.add_employee_name("Sally")
c1.add_funding(50000)
print(c1.employee_list, '= c1 employee list')
print(c1.employee_count, '= c1 employee count')
print(c1.funding_amount, '= c1 funding amount')

c2 = Company()
c2.add_funding(10000000)
c2.add_funding(50000)
c2.add_employee_name('Bob')
print(c2.employee_list, '= c2 employee list')
c2.add_employee_name('Joe')
print(c2.employee_list, '= c2 employee list')
print(c2.employee_count, '= c2 employee count')
print(c2.funding_amount, '= c2 funding amount')