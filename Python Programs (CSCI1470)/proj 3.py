#**********************  Proj1.py  *********************
#
# Name: Hailey Thomas
#
# Algorithm
#   Gives exact change for an item purchased with $5 or less. Use a float data type to represent money
#   Correct number of dollar bills, quarters, dimes, nickels, and pennies. 
#   Inputs item cost and amount tendered  in float format 
#   Correctly calculates the exact change 
#
#************************************************************************


item_cost = float(input('Enter item cost: '))
tender = float(input('Enter amount tendered: '))


change = int((tender - item_cost) * 100)


dollars = change // 100
change = change % 100
quarters = change // 25
change = change % 25
dimes = change // 10
change = change % 10
nickels = change // 5
change = change % 5
pennies = change 


if dollars == 1:
    print('Dollar:', dollars)
else:
    print('Dollars:', dollars)

if quarters == 1:
    print('Quarter:', quarters)
else:
    print('Quarters:', quarters)

if dimes == 1:
    print('Dime:', dimes)
else:
    print('Dimes:', dimes)
    
if nickels == 1:
    print('Nickel:', nickels)
else:
    print('Nickels:', nickels)

if pennies == 1:
    print('Penny:', pennies)
else:
    print('Pennies:', pennies)
    
