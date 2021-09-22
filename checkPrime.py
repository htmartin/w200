#checkPrime(num):
num =13
x=2
while x < num :
    print(x,'<=', num)
    
    if num % x ==0:
        print(x)
        print("Not Prime!")
        break
    x+=1
else:
    print("Prime!")     
   
# 2 <= 25
# 3 <= 25
# 4 <= 25
# 5 <= 25
# 5
# Not Prime!
# Prime!

checkPrime(num):
    x=2
    while x < num :
        print(x,'<=', num)
    
        if num % x ==0:
            print(x)
            print("Not Prime!")
            break
        x+=1
    else:
        print("Prime!")     