###############################     ThomasH_CSCI1470_Proj6.py       ###################################
#  Name: Hailey Thomas
#
#  Course: CSCI 1470
#
#  Assignment: Program 6
#  
#  Algorithm:
#    Write a function named convert( ) that takes any string of alphanumeric
#    characters and returns a string with all alphabetic characters in the argument
#    converted into their numeric equivalent, using the above mapping.
#    Write a Python program that asks the user to enter a 10-character alphanumeric
#    telephone number in the form of XXX-XXX-XXXX, then calls convert( ) 
#    to translate the alphanumeric phone number into its equivalent numeric phone number
#    and display the result. 
#    The application should allow the user to continue translating phone numbers
#    until she/he decides to stop.
#    Use meaningful variable names. Prepend a preface.
################################################################################


def convert():

    phoneNum = input('Enter the number in the format of XXX-XXX-XXXX. Make sure any letters are capitalized: ')
    newPhoneNumber = ''
    
    for char in phoneNum:
        if char == 'A' or char == 'B' or char == 'C':
            char = '2'
        elif char == 'D' or char == 'E' or char == 'F':
            char = '3'
        elif char == 'G' or char == 'H' or char == 'I':
            char = '4'
        elif char == 'J' or char == 'K' or char == 'L':
            char = '5'
        elif char == 'M' or char == 'N' or char == 'O':
            char = '6'
        elif char == 'P' or char == 'Q' or char == 'R' or char == 'S':
            char = '7'
        elif char == 'T' or char == 'U' or char == 'V':
            char = '8'
        elif char == 'W' or char == 'X' or char == 'Y' or char == 'Z':
            char = '9'
            
        newPhoneNumber = newPhoneNumber + char

    print(newPhoneNumber)
 


convert()
