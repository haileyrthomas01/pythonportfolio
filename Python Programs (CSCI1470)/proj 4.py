#**********************  ThomasH_CSCI1470_Proj1.py  *********************
#
# Name: Hailey Thomas
#
# Course: CSCI 1470
#
# Assignment: Program #4
#
# Algorithm
#   Prompt user for weights of boxing competitors between 51-64kg
#   Accept weights of competitors until zero or negative number entered 
#   Determine who how many competitors in each category
#   If zero comptetitors in a category, do not list it
#   If there is only one competitor in a category,
#   add one to the next higher category if there is one
#   If there is a single welterweight, do not move this
#   competitor from the category
#   If a competitor weight is below 51 or above 64, add
#   them to one of two new categories: TooLow, TooHigh
#   Calculate and print the average weight of all competitors in the competition.
#
#************************************************************************

welterweight = 0
lightweight = 0
featherweight = 0
bantamweight = 0
tooHigh = 0
tooLow = 0

sumWeights = 0
numWeights = 0
avgWeight = 0

weight = int(input("Enter weights for boxing competitors ('0' or negative number to quit): "))

while (weight != 0) and (not weight < 0):
    sumWeights += weight
    numWeights += 1
    weight = int(input("Enter weights for boxing competitors ('0' or negative number to quit): "))
    avgWeight = sumWeights / numWeights


    if (weight >= 61 and weight <= 64):
        welterweight += 1


    elif (weight >= 58 and weight <= 60):
        lightweight += 1

        if (lightweight == 1):
            welterweight += 1
            
    elif (weight >= 55 and weight <= 57):
        featherweight += 1

        if (featherweight == 1):
            lightweight += 1
            
    elif (weight >= 51 and weight <= 54):
        bantamweight += 1
            
        if (bantamweight == 1):
            featherweight += 1


    elif (weight < 51) and (weight > 0):
        tooLow += 1

        
    elif (weight > 64):
        tooHigh += 1





    if (weight == 0):
        print()
        print("The average weight of all competitors in the competition is", avgWeight)
        print("There are", tooLow, "competitors that are too low to compete.")
        print("There are", tooHigh, "competitors that are too high to compete.")

        printWelZero = "There are no welterweight competitors."
        printLigZero = "There are no lightweight competitors."
        printFeaZero = "There are no featherweight competitors."
        printBanZero = "There are no bantamweight competitors."


        if (welterweight == 0):
            print(printWelZero)
        else:
            print("There are", welterweight, "welterweight competitors.")

        if (lightweight == 0):
            print(printLigZero)
        else:
            print("There are", lightweight, "lightweight competitors.")

        if (featherweight == 0):
            print(printFeaZero)
        else:
            print("There are", featherweight, "featherweight competitors.")

        if (bantamweight == 0):
            print(printBanZero)
        else:
            print("There are", bantamweight, "bantamweight competitors.")
