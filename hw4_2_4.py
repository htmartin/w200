# Implement this digit-by-digit algorithm to find the square root of x 
#to a precision of epsilon.

# Begin with a step size of 1 and guess of zero.
# Increase the guess by the step size as long as doing so 
#would not cause the guess^2 to exceed x. 
# Repeat this step (step 2) 
# until the next repetition will cause guess^2 to exceed x.
# If the step size is greater than or equal to epsilon, 
# then divide the step size by 10 and go back to step 2.
# Notice that once a digit has been found, it is not changed again. 
# Try using your code to find the square 
# root of 10 to an epsilon of 10 decimal places. 
# This algorithm should not take over 30 seconds to run 
# (if it does you have coded something incorrectly!).

# If you are getting an answer that is off by epsilon 
# (for example 3.1622776602 instead of 3.1622776601), 
# this might be caused by the floating point error. 
# You can read more about that here: 
#     https://docs.python.org/3/tutorial/floatingpoint.html. 
#         To fix this problem, you can use the 
#         Decimal library here: 
# https://docs.python.org/3/library/decimal.html#module-decimal

# Hint: It might be helpful to write out by hand an easier example 
# like '4' to understand how the algorithm works.

# Example output:

# Enter a number to find the square root: 10
# The square root of 10 is 3.1622776601.

# Begin with a step size of 1 and guess of zero.
x =10
step_size = 1  
guess = 0
epsilon = .0000001
num_guesses = 0

# S2:
#Increase the guess by the step size as long as doing so 
#would not cause the guess^2 to exceed x. 

# Repeat this step (step 2) 
# until the next repetition will cause guess^2 to exceed x.
# If the step size is greater than or equal to epsilon, 
# then divide the step size by 10 and go back to step 2.

while guess**2 < x:
    guess += step_size
    num_guesses+=1
    if guess**2 > x:
        break
    print('x =',x, 'guess^2 =', guess**2)
    if step_size >= epsilon:
        step_size =step_size/10
        print('step_size =',step_size, 'guess =', guess, 'num_guesses =', num_guesses)
        
        
        
# Try using your code to find the square 
# root of 10 to an epsilon of 10 decimal places. 