
item_cost = float(input('Enter item cost: '))
amount_tendered = float(input('Enter the amount tendered: '))

change = amount_tendered - item_cost

cents = int(change * 100)
dollars = cents // 100
quarters = (cents - 100 * dollars) // 25
dimes = (cents - 100 * dollars - 25 * quarters) // 10
nickels = (cents - 100 * dollars - 25 * quarters - 10 * dimes) // 5
pennies = (cents - 100 * dollars - 25 * quarters - 5 * nickels)

print("Dollars: ", dollars)
print("Quarters: ", quarters)
print("Dimes: ", dimes)
print("Nickels: ", nickels)
print("Pennies: ", pennies)
