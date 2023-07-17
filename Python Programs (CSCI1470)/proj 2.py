#**********************  proj2.py  *********************
#
# Name: Hailey Thomas
#
#
# Assignment: Program #2
#
# Algorithm:
#  - Stores low daily temperatures in a list called low_daily_temperatures
#  - Stores high daily temperatures in a list called high_ daily_temperatures
#  - Determines and prints the minimum temperature in the week
#  - Determines and prints the maximum temperature in the week
#  - Calculates and prints the average of low temperatures and
#    the average of high temperatures in the week
#  - Calculates and prints the difference between average low and average
#    high temperatures
#
#************************************************************************


#  Stores low daily temperatures in a list called low_daily_temperatures
#  and stores high daily temperatures in a list called high_ daily_temperatures
low_daily_temperatures = [75, 77, 76, 78, 72, 70, 70]
high_daily_temperatures = [90, 92, 92, 93, 91, 89, 88]

#  Determines and prints the minimum temperature in the week
#  and determines and prints the maximum temperature in the week
min_temp = (min(low_daily_temperatures))
print ('Minimum temperature in the week:', min_temp, 'degrees')

max_temp = (max(high_daily_temperatures))
print ('Maximum temperature in the week:', max_temp, 'degrees')

#  Calculates and prints the average of low temperatures and
#  the average of high temperatures in the week
avg_low = sum(low_daily_temperatures)/len(low_daily_temperatures)
print('Average of low temperature:', avg_low)

avg_high = sum(high_daily_temperatures)/len(high_daily_temperatures)
print('Average of high temperature:', avg_high)

#  Calculates and prints the difference between average low and average
#  high temperatures
diff_low_and_high = avg_low - avg_high
print('The difference between the average low temperature and the average high temperature is:', diff_low_and_high)

