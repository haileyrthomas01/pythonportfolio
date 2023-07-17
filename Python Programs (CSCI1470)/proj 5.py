###############################     ThomasH_CSCI1470_Proj5.py       ###################################
#  Name: Hailey Thomas
#
#  Course: CSCI 1470
#
#  Assignment: Program 5
#  
#  Algorithm:
#    Design and write a Python program that gives and grades a math quiz.
#    The quiz will give 10 random problemsusing a variety of the
#    arithmetic operators: +, -, *, //, and % and grade the quiz.
#    Your program will generate a problem for the user to answer in the form of: 
#    num1 op num2  = 
#    and the user will then type an answer.
#    The user enters an answer that is correct or incorrect.
#    If the answer is correct, a message is printed and 1 is added to the
#    number of correct answers.
#    Then another problem is given and checked, and so on, until ten problems
#    have been given and checked.
#    Make a list of the characters for the operators
#    Your main program generates the random operator and the random numbers and
#    calls the appropriate function for that operator.
#    Define a function for each of the 5 operators.
#    The main program passes that function the two random numbers.
#    Each function displays the problem, gets the user input,
#    and determines if the answer is correct or incorrect.
#    If the answer is correct, the function returns a value of 1,
#    and if incorrect, the function will return a value of 0.
#    After ten problems have been given, the main program prints out the total score of
#    that quiz, and asks the user if she/he wants to take another quiz.
#    The main program keeps giving a quiz as long as the user wants to continue.
#
#    For division use // and do floor division.
#
#    Please pay attention to the difference between “+” and +. The string can be used for comparison
#    and the operator can be used to determine the correct answer.
#####################################################################################

import random

num1 = 0
num2 = 0
score = 0

    
ops = ['+', '-', '*', '//', '%']

print('Welcome. This is a 10 question math quiz.')

def numQuiz(num1, num2, i):

    operator = ops[i]
    
    print("Here's your question: "+ str(num1)+ ops[i]+ str(num2))
    userInputInt = int(input("What's your answer? "))

    if operator == '+':
        answer = num1 + num2

    elif operator == '-':
        answer = num1 - num2

    elif operator == '*':
        answer = num1 * num2

    elif operator == '//':
        answer = num1 // num2

    else:
        answer = num1 % num2
   

    if answer == userInputInt:
        print('Correct!\n')
        return 1
    else:
        print('Incorrect!\n')
        return 0 

print("Do you want to take a quiz? (Yes or No)")


running = input()


while running == 'Yes':
    
    print("Alright, let's begin the quiz!")
    for i in range(10):

        index = random.randint(0,4)
        num1 = random.randint(1,20)
        num2 = random.randint(1,20)    
        temp = numQuiz(num1, num2, index)


        if temp == 1:
            score += 1

    print("Thank you for playing! You're score is", score)
    print("Do you want to take another quiz? (Yes or No)")
    running = input()



