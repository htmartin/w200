income = input ('Please enter your income:')

if int(income) <= 1000:
    print ('The tax owed is:', int(income)*.05)
elif 1000 < int(income) <= 2000:
    print ('The tax owed is:', (int(income)*.1))
elif int(income) > 2000:
    print ('The tax owed is:', (int(income)*.15))