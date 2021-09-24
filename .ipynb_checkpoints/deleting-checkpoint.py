# 4-3-4. Given a word, provided below, use a single comprehension to make a list of all strings that can be formed by deleting exactly one character from the word.

# Required output: 
#word = "Welcomed"

# ['elcomed', 'Wlcomed', 'Wecomed', 'Welomed', 'Welcmed', 'Welcoed', 'Welcomd', 'Welcome']
word = "Welcomed"
delete_letter = []
for i in range(0,len(word)):
    delete_letter.append(word.replace(word[i],''))
    print(delete_letter)
    
#LC  
word = "Welcomed"
delete_letter = [word.replace(word[i],'') for i in range(0,len(word))]
print(delete_letter)
    
    
    
# 4-3-5. Given a word, provided below, use a single comprehension to make a list of all strings that can be formed by replacing exactly one vowel in the word with a different vowel (a vowel is a,e,i,o,u).

# Required output:word = "Booted"

# ['Baoted', 'Beoted', 'Bioted', 'Buoted', 'Boated', 'Boeted', 'Boited', 'Bouted', 'Bootad', 'Bootid', 'Bootod', 'Bootud']


word = "Booted"
vowels= [a,e,i,o,u]

rep_vowels =[]
for i in word:
    if i in vowels:
        for r in range(0,len(vowels)):
        print(vowels[i])
        #print(word.replace(i,vowels[i+1]))