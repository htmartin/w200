#!/usr/bin/env python

price = input("Enter the price of a meal: ")
#price =30
price = float(price)

tip_rate = .16

tip = price * tip_rate

total = price + tip

print("A 16% tip would be:", tip)
print("The total including tip would be:", total)