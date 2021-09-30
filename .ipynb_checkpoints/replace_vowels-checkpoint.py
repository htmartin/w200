# use a single comprehension 
# to make a list of all strings that can be formed by replacing 
# exactly one vowel in the word 
# with a different vowel (a vowel is a,e,i,o,u).

# Required output:

# ['Baoted', 'Beoted', 'Bioted', 'Buoted', 
#  'Boated', 'Boeted', 'Boited', 'Bouted', 
#  'Bootad', 'Bootid', 'Bootod', 'Bootud']

word = "Booted"
vowels = 'aeiou'#['a','i','e','o','u']

replace_vowels =[]
for i in word:
    if i in vowels:
        for v in vowels:
            if i != v:
                replace_vowels.append(word.replace(i,v))
                print(replace_vowels)
                
#print(word.replace(i,vowels[r]))
            
            
# exactly one vowel in the word 
first, replace first vowel in word with every other vowel,
second, replace second vowel in word with every other vowel,
etc for all vowels in word 
but not if it doesn't change the word

lala = "Booted"
parts=[]
for l in word:
    if l in vowels:
        a = word before vowel
        b = loop over vowels
        c = word after vowel
        parts.append(a+b+c)
        
        
lala = "Booted"
vowels = 'aeiou'
parts=[]
for i in range(0,len(lala)): #0, 1, 2, 3, 4, 5
    if lala[i] in vowels:
        parts.append(lala[:i]+vowels[0]+lala[i+1:])
        #parts.append(lala[i+1:])
        print(parts)
        
        Get:
['B', 'oted']
['B', 'oted', 'Bo', 'ted']
['B', 'oted', 'Bo', 'ted', 'Boot', 'd']


word = "Booted"
vowels = 'aeiou'
parts=[]
for i in range(0,len(word)): #0, 1, 2, 3, 4, 5
    if word[i] in vowels:
        for v in range(0,len(vowels)):
            if v != word[i]:
                parts.append(word[:i]+vowels[v]+word[i+1:])
                print(parts)

['Baoted', 'Beoted', 'Bioted', 'Booted', 'Buoted', 
 'Boated', 'Boeted', 'Boited', 'Booted', 'Bouted', 
 'Bootad', 'Booted', 'Bootid', 'Bootod', 'Bootud']

parts=[word[:i]+vowels[v]+word[i+1:] for i in range(0,len(word)) if word[i] in vowels for v in range(0,len(vowels)) if v !=word[i] ]

print(parts)