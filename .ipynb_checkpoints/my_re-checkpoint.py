import re
source = 'Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.'

pattern ='.*high-level'
result = re.match(pattern, source)
print(result)
<re.Match object; span=(0, 34), match='Python is a widely used high-level'>

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