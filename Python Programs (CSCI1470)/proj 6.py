###############################     Proj6.py       ###################################
#  
#  Algorithm:
#    Write a function named convert( ) that takes any string of alphanumeric
#    characters and returns a string with all alphabetic characters in the argument
#    converted into their numeric equivalent, using the above mapping.
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
