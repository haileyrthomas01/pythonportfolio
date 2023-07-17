#**********************  ThomasH_CSCI1470_Proj8.py  *********************
#
# Name: Hailey Thomas
#
# Course: CSCI 1470
#
# Assignment: Program #8
#
# Algorithm
#   Make a code for a card game called Battle
#   Two players have a card deck consisting of 
#   One card deck could be represented by two parallel lists:
#   one list has the card names and one has the corresponding card value. 
#   Both players have a card randomly selected using a random number (using random.randint()).
#   When a card is selected, print the name of the card as given in the cardNames list. 
#   The player that plays the card with a higher value in the cardValues list) wins a point for that round
#   If both cards have the same value, neither receives a point.
#   Remove the card name and the card value from the respective lists for both players.
#   You will want to print the lists to verify that the selected card has been deleted from the deck.
#   Continue to play until all 13 cards have been played.
#   Display each card played in each round and the current scores.
#   Print the final scores and pronounce the one with the highest score as the winner.
#   Allow the user of the game to continue as long as the user wishes.

#************************************************************************
import random

#cardNamesPlayer1 = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
#                    "jack", "queen", "king", "ace"]
#cardValuesPlayer1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#cardNamesPlayer2 = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
#                    "jack", "queen", "king", "ace"]
#cardValuesPlayer2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print("Welcome to the game 'Battle'! Would you like to play? (Type Yes or No)")

def battle():

    playerOnePoints = 0
    playerTwoPoints = 0

    cardNamesPlayer1 = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                    "jack", "queen", "king", "ace"]
    cardValuesPlayer1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    cardNamesPlayer2 = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                    "jack", "queen", "king", "ace"]
    cardValuesPlayer2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    
    while len(cardNamesPlayer1) != 0:

        player1 = random.choice(cardValuesPlayer1)
        player2 = random.choice(cardValuesPlayer2)

        if player1 == 2:
            print("Player 1's card is", cardNamesPlayer1[cardValuesPlayer1.index(2)])

        elif player1 == 3:
            print("Player 1's card is", cardNamesPlayer1[cardValuesPlayer1.index(3)])

        elif player1 == 4:
            print("Player 1's card is", cardNamesPlayer1[cardValuesPlayer1.index(4)])

        elif player1 == 5:
            print("Player 1's card is", cardNamesPlayer1[cardValuesPlayer1.index(5)])

        elif player1 == 6:
            print("Player 1's card is", cardNamesPlayer1[cardValuesPlayer1.index(6)])

        elif player1 == 7:
            print("Player 1's card is", cardNamesPlayer1[cardValuesPlayer1.index(7)])

        elif player1 == 8:
            print("Player 1's card is", cardNamesPlayer1[cardValuesPlayer1.index(8)])

        elif player1 == 9:
            print("Player 1's card is", cardNamesPlayer1[cardValuesPlayer1.index(9)])

        elif player1 == 10:
            print("Player 1's card is", cardNamesPlayer1[cardValuesPlayer1.index(10)])

        elif player1 == 11:
            print("Player 1's card is", cardNamesPlayer1[cardValuesPlayer1.index(11)])

        elif player1 == 12:
            print("Player 1's card is", cardNamesPlayer1[cardValuesPlayer1.index(12)])

        elif player1 == 13:
            print("Player 1's card is", cardNamesPlayer1[cardValuesPlayer1.index(13)])

        elif player1 == 14:
            print("Player 1's card is", cardNamesPlayer1[cardValuesPlayer1.index(14)])
        else:
            print()
            

        if player2 == 2:
            print("Player 2's card is", cardNamesPlayer2[cardValuesPlayer2.index(2)])

        elif player2 == 3:
            print("Player 2's card is", cardNamesPlayer2[cardValuesPlayer2.index(3)])

        elif player2 == 4:
            print("Player 2's card is", cardNamesPlayer2[cardValuesPlayer2.index(4)])

        elif player2 == 5:
            print("Player 2's card is", cardNamesPlayer2[cardValuesPlayer2.index(5)])

        elif player2 == 6:
            print("Player 2's card is", cardNamesPlayer2[cardValuesPlayer2.index(6)])

        elif player2 == 7:
            print("Player 2's card is", cardNamesPlayer2[cardValuesPlayer2.index(7)])

        elif player2 == 8:
            print("Player 2's card is", cardNamesPlayer2[cardValuesPlayer2.index(8)])

        elif player2 == 9:
            print("Player 2's card is", cardNamesPlayer2[cardValuesPlayer2.index(9)])

        elif player2 == 10:
            print("Player 2's card is", cardNamesPlayer2[cardValuesPlayer2.index(10)])

        elif player2 == 11:
            print("Player 2's card is", cardNamesPlayer2[cardValuesPlayer2.index(11)])

        elif player2 == 12:
            print("Player 2's card is", cardNamesPlayer2[cardValuesPlayer2.index(12)])

        elif player2 == 13:
            print("Player 2's card is", cardNamesPlayer2[cardValuesPlayer2.index(13)])

        elif player2 == 14:
            print("Player 2's card is", cardNamesPlayer2[cardValuesPlayer2.index(14)])

        else:
            print()


        if player1 > player2:
            playerOnePoints += 1
            print("Player 1 has earned a point! Congratulations!")

        elif player1 < player2:
            playerTwoPoints += 1
            print("Player 2 has earned a point! Congratulations!")

        else:
            cardNamesPlayer1.pop(cardValuesPlayer1.index(player1))
            cardNamesPlayer2.pop(cardValuesPlayer2.index(player2))
            cardValuesPlayer1.pop(cardValuesPlayer1.index(player1))
            cardValuesPlayer2.pop(cardValuesPlayer2.index(player2))
        
        print("Player 1's cards are:", cardNamesPlayer1)
        print("Player 2's cards are:", cardNamesPlayer2)
        print("Player 1 has", playerOnePoints, "points and Player 2 has", playerTwoPoints, "points.")

    if playerOnePoints > playerTwoPoints:
        print("Congratulations Player 1! You won with", playerOnePoints, "points! You win!")
    elif playerOnePoints < playerTwoPoints:
        print("Congratulations Player 2! You won with", playerTwoPoints, "points! You win!")
    else:
        print("Oh no! Player 1 and Player 2 are tied!", playerOnePoints, playerTwoPoints)

running = input()

while running == 'Yes':
    battle()
    print("Do you want to play again? (Yes or No)")
    running = input()
