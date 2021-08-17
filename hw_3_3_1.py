x#!/usr/bin/env python



# script that allows user to input name

name = 'Joe Blow'
###name = input('Please enter your name:')
# split the resulting string to create a list of the name parts.
list_name = list(name.split())

# iterate over list_name
#     for each name part(np)
#         uncap the start letter
            # iterate over np strings
#         move the start letter to the end of the name part
#         append the letters "ay" to the end of the resulting name part
#         cap the name part

lower_list_name=[]

for i in list_name:
    
    np=i.lower()
    lower_list_name.append(np)
    
    #lower np strings need to be in a new list
# iterate over np strings
pl_list =[]
for i in lower_list_name:
#separate each name part into a list of its letters e.g., ['j', 'o', 'e']
    a = list(i)
    #print(a)
    #         move the start letter to the end of the name part e.g., ['o', 'e', 'j']

    b=list(a[1:])
    c=list(a[0])
    d=b+c
    #print(d)
#         append the letters "ay" to the end of d(the resulting name part)e.g., ['o', 'e', 'j', 'a','y']
    e= list('ay')
    f = d + e
    g= ''.join(f)
   #turn each name part letter list back into string e.g., 'oejay'
    h=str(g)
    print(h)
     # ??? cap each name part e.g., Oejay
    #for i in h:
        #cap_word=i.title()
        #print(cap_word)
   

    #add each resulting name part str back into pl(list of strings with whole names)['Oejay', 'Lowbay']
    pl_list.append(h)
    print(pl_list) #['oejay', 'lowbay']
    # ??? there could be more than 2 name parts? Let's get it working with just the two name version first:
    
   # j= pl_list[0]
   # k = pl_list[1]
   # print ('Your name in pig latin is:' j, k)