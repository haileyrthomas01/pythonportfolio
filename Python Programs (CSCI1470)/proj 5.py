###############################     Proj5.py       ###################################

#  Algorithm:
#    Design and write a Python program that gives and grades a math quiz.
#    The quiz will give 10 random problems using a variety of the
#    arithmetic operators: +, -, *, //, and % and grade the quiz.
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



