#**********************  proj1.py  *********************
#
# Name: Hailey Thomas
#
#
# Assignment: Program #1
#
# Algorithm
#   Input emplyee's name, hourly wage, total regular hours,
#   and total overtime hours for the week
#   Get inputs for employee & calculate total weekly pay for employee
#   Calculate overtime pay
#   Display name of employee with total pay amount for the week
#
#************************************************************************

# Declare variables

employee_name = input('What is your full name? ')
hourly_wage = float(input('What is your hourly wage? '))
regular_hours = float(input('How many regular hours have you worked? '))
overtime_hours = float(input('How many overtime hours have you worked? '))

# Calculate values

regular_pay = regular_hours * hourly_wage
overtime_pay = overtime_hours * (1.5 * hourly_wage)
weekly_pay = regular_pay + overtime_pay

# Print employee name and weekly pay

print(employee_name, 'your total pay amount for the week is $', weekly_pay)



