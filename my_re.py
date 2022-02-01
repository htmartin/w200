import re
source = 'Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.'

pattern ='.*high-level'
result = re.match(pattern, source)
print(result)
#<re.Match object; span=(0, 34), match='Python is a widely used high-level'>

joe = re.compile('.*high-level')
bob = joe.match(source)
if bob:
    print(bob.group())
    
    joe = re.compile('high-level')
bob = joe.search(source)
if bob:
    print(bob.group())
    
    
#all the matches


sal = re.compile('p')
ugh = sal.findall(source)
if ugh:
    print( 'Found', len(ugh), 'matches')
    
sal = re.compile('p.')
ugh = sal.findall(source)
if ugh:
    print( 'Found', len(ugh), 'matches')

sal = re.compile('p?')
ugh = sal.findall(source)
if ugh:
    print( 'Found', len(ugh), 'matches')
    
Found 11 matches
Found 11 matches
Found 272 matches


# split at matches with split 
sal = re.compile('high-level')
ugh = sal.split(source)
if ugh:
    print( ugh)
    
#replace matches with sub

#Drill
# Using the sample text below and regular expressions find the place where the world 'involuntarily' appears (find the string slice).

text = """Call me Ishmael. Some years ago - never mind how long precisely - having little or no money in my purse, 
and nothing particular to interest me on shore, I thought I would sail about a little and see the watery 
part of the world. It is a way I have of driving off the spleen and regulating the circulation. 
Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; 
whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; 
and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me 
from deliberately stepping into the street, and methodically knocking people's hats off - then, 
I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. 
With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. 
There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, 
cherish very nearly the same feelings towards the ocean with me."""


# Using the text from 9.7.1 above find how many times the word 'I' is used.
sal = re.compile('I')
ugh = sal.findall(text)
if ugh:
    print( 'Found', len(ugh), 'matches')
    
    #12

# counts of how people paid. That is, get the count of each of these codes:
# O = Online, P = Phone, Cash = Cash, CC = Credit Card

pay_list = ['O[SGC] Paid $123.34', 'Cash - $150.00 - ABC', 'O[ABC] Paid $230.23', 'P[rjf@abc.net] paid 321.12', 
            'O[CGR] Paid $967.21', 'CC[ajk] 245.34', 'P[abc@rjf.net] paid 161.13', 'Cash - $100.00 - rjf', 
            'Cash - $100.00 - gun', 'O[DYTC] Paid $199.99', 'O[ABC] Paid $123.93', 'P[dtc@dtc.com]  paid 109.56',
            'CC[ABC] 186.70', 'CC[CGC] 995.95', 'Cash - $125.00 - pal']

n = str(pay_list)
n

codes = ['O', 'P','Cash', 'CC']
for i in codes:
    a = re.compile(i)
    b = a.findall(n)
    if b:
        print( 'Found', len(b), 'matches for the code', i)

Found 5 matches for the code O
Found 8 matches for the code P
Found 4 matches for the code Cash
Found 3 matches for the code CC
# 4. Using regular expressions and the pay_list from above, find the total amount of money that was paid. 


phone_number_pattern= 
re.compile(r'[0123456789]{3}-[0123456789]{3}-[0123456789]{4}')
m = phone_number_pattern.findall(large_source)
print(m)

phone_number_pattern= 
re.compile(r'\d{3}-\d{3}-\d{4}')
m = phone_number_pattern.findall(large_source)
print(m)