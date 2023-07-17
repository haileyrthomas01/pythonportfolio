############################### ThomasH_CSCI1470_Proj9.py ############################
#  Name: Hailey Thomas
#
#  Course: CSCI 1470
#
#  Assignment: Program 9
#
#  Algorithm:
#   Convert the Gettys2.txt file in your Files folder under Content in Blackboard
#   into a new file that contains only the words without the letter ‘e’ in them
#   For each line of the file, create a new string containing only the words
#   that do not contain the letter ‘e’.
#   Write each revised line out to an output file named GettysNoE.txt.
#   Use a function hasNoE( ) that returns True if a given word doesn’t have
#   the letter ‘e’ in it. 
#   Submit your output file along with your .py file.
#
#####################################################################################

gettysburg = open('/Users/haileythomas/Downloads/comp sci csci1470/IDLE HMWK/Gettys2.txt')

for word in gettysburg:
    if "e" in word:
        print(word)

gettysburg.close()
