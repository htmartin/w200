### Q3-1 Grading Tag: Please put your entire solution in this cell. Don't edit this line.


###This is working program before I started on n nps.



# script that allows user to input name

#name = 'Joe Blow'
name = input('Please enter your name:')
# split the resulting string to create a list of the name parts.
list_name = list(name.split())

# iterate over list_name
#     for each name part(np)
#         uncap the start letter
#add resulting nps to new list lower_list_name

lower_list_name=[]

for i in list_name:
    
    np=i.lower()
    lower_list_name.append(np)
            # iterate over np strings
#         move the start letter to the end of the name part
#         append the letters "ay" to the end of the resulting name part
#         cap the name part    
    #lower np strings need to be in a new list
# iterate over np strings
pl_list =[]
#         move the start letter to the end of the name part
for i in lower_list_name:
#separate each name part into a list of its letters e.g., ['j', 'o', 'e']
    a = list(i)
    #print(a)
    #         move the start letter to the end of the name part e.g., ['o', 'e', 'j']

    b=list(a[1:])
    c=list(a[0])
    d=b+c
    #print(d)
#   append the letters "ay" to the end of d(the resulting name part)e.g., ['o', 'e', 'j', 'a','y']
    e= list('ay')
    f = d + e
    
#turn each name part letter list back into string e.g., 'oejay'
    g= ''.join(f)
    #print(g)
    h=str(g)
#add each resulting name part str back into pl(list of strings with whole names)['oejay', 'lowbay']
    pl_list.append(h)
    #print(pl_list) #['oejay', 'lowbay']

# cap each name part in str pl_list e.g., ['Oejay', 'Lowbay']
pl_list_upper = []

for i in pl_list:
    cap_word=i.title()
    #print(cap_word)
    pl_list_upper.append(cap_word)
    #print(pl_list_upper) -> ['Oejay', 'Lowbay']
    
# print full name in pig latin, e.g., Oejay Lowbay    
# get it working with just the two name part version first (there could be more than 2 name parts? )
    
j= pl_list_upper[0]
print (j)
k = pl_list_upper[1]
print (k)
print (j, k)
print ('Your name in pig latin is:', j, k)


    # ??? there could be more than 2 name parts?  print re-creation of: Enter your name: Paul Laskowski-> Aulpay Askowskilay
