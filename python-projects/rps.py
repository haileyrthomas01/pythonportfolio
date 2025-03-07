import random 

print("===================")
print("Rock Paper Scissors")
print("===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")

pick = int(input("Pick a number: "))
cpu = random.randint(1,3)

## Player
if pick == 1:   
    print("You chose: ✊")
elif pick == 2:
    print("You chose: ✋")
elif pick == 3:
    print("You chose: ✌️")

## CPU
if cpu == 1:   
    print("CPU chose: ✊")
elif cpu == 2:
    print("CPU chose: ✋")
elif cpu == 3:
    print("CPU chose: ✌️")

## Player vs. CPU
if (pick==1 and cpu==1) or (pick==2 and cpu==2) or (pick==3 and cpu==3):
    print("Tie!")

elif (pick==2 and cpu==1): 
    print("The player won!")

elif (pick==3 and cpu==1):
    print("The CPU won!")

elif (pick==2 and cpu==3):
    print("The CPU won!")

elif (pick==3 and cpu==2):
    print("The player won!")

elif (pick==1 and cpu==2):
    print("The CPU won!")

elif (pick==1 and cpu==3):
    print("The player won!")


