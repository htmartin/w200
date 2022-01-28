import string
printable = string.printable
print(printable)

re.findall('\d', printable)
re.findall('\w', printable)
re.findall('\s', printable)


# Using specifiers- just giant table
#find a phone #
import re
large_source = 'Python is a 303-655-9362 widely used high-level, general-purpose, interpreted, dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.'

phone_number_pattern= 
re.compile(r'[0123456789]{3}-[0123456789]{3}-[0123456789]{4}')
m = phone_number_pattern.findall(large_source)
print(m)

phone_number_pattern= 
re.compile(r'\d{3}-\d{3}-\d{4}')
m = phone_number_pattern.findall(large_source)
print(m)

###Specifying match output

phone_number_pattern= 
re.compile(r'(\d{3})-(\d{3}-\d{4})')
m = phone_number_pattern.search(large_source)
if m:
	print(m.group)
	print(m.groups)


#name the groups
phone_number_pattern= 
re.compile(r'(?P<areacode>\d{3})-(?P<number>\d{3}-\d{4})')
m = phone_number_pattern.search(large_source)
if m:
	print(m.group('areacode'))
	print(m.groups('number'))
