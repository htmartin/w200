gallons = input("Enter the number of gallons of gasoline: ")

liters = float(gallons)* 3.7854

liters= "{:.4f}".format(liters)

barrels = float(gallons)/19.5

barrels= "{:.3f}".format(barrels)

gas_price = float(gallons)* 3.65

gas_price= "{:.2f}".format(gas_price)

print(gallons, 'gallons is ', liters, 'liters.')

print(gallons, 'gallons takes ', barrels, 'barrels.')

print('The price of', gallons, 'gallons', 'is $', gas_price,'.')