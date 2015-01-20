import random
import sys

#Guess the Number
# In this game, the user tries to guess the number thought up by the computer.
# The number is between 0 and 99.


#TO DO - Figure out a way to get rid of casting; instead check if number, then cast?
#      - Put the text in functions that return strings


#FUNCTIONS

def welcomeText() :
    return "My name is The Number NINJA and I doubt you can guess what\n"
    "number I\'m thinking of. It\'s between 0 and 99, but what it is... \n"
    "you\'ll never know. So go ahead, take a guess... and fail."


def userTooBig() :
    randomNum = random.randrange(0,1000)
    if randomNum % 2 == 0 :
        "Ha, ha. Think smaller! Or you will have no chance in figuring it out."
    else:
        "Wrong wrong wrong! More isn't always better"


def userTooSmall() :
    randomNum = random.randrange(0,1000)
    if randomNum % 2 == 0:
        "Ha, ha you are wrong! My number is way bigger than you think!"
    else:
        "Nope!! You underestimate the power of my NUMBER"


def goodByeText(my_num) :
    return "No, no, no! You figured out my secret number, %d! You must be some kind of mastermind \n"
    "in the works. Grrr....Go ahead. Tell all your friends you have beaten me, the Master of \n" \
    "All Numbers. You are now the new Number Ninja!"%(my_num)


my_number = random.randrange(0,100)

print(welcomeText())
userInput = int(sys.stdin.readline())
while userInput != my_number:
    if userInput < my_number:
        print(userTooSmall())
        userInput = int(sys.stdin.readline())
    else :
        print(userTooBig())
        userInput = int(sys.stdin.readline())

print(goodByeText(my_number))
