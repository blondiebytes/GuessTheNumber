import random
import sys

#Guess the Number
# In this game, the user tries to guess the number thought up by the computer.
# The number is between 0 and 99.


#TO DO - Figure out a way to get rid of repeat-code


#FUNCTIONS

def welcomeText() :
    return "My name is The Number NINJA and I doubt you can guess " \
           "what\nnumber I\'m thinking of. It\'s between 0 and 99, " \
           "but what it is... \nyou\'ll never know. So go ahead, " \
           "take a guess... and fail."


def userTooBig() :
    randomNum = random.randrange(0,1000)
    if randomNum % 2 == 0 :
        return "Ha, ha. Think smaller! Or you will have no chance in figuring it out."
    else:
        return "Wrong wrong wrong! More isn't always better"


def userTooSmall() :
    randomNum = random.randrange(0,1000)
    if randomNum % 2 == 0:
       return "Ha, ha you are wrong! My number is way bigger than you think!"
    else:
        return "Nope!! You underestimate the power of my NUMBER!"

def isInputNum(user_input):
    return user_input.isdigit

def inputChecker(user_input):
    if not isInputNum(user_input):
        raise Exception("Ha, ha, you don't even know what a number is!")

def goodByeText(my_num) :
    return "No, no, no! You figured out my secret number, %d! You must be some kind of mastermind \n" \
    "in the works. Grrr.... Go ahead. Tell all your friends you have beaten me, the Master of \n" \
    "All Numbers. You are now the new Number Ninja!"%(my_num)


my_number = random.randrange(0,100)

# What we actually run....
print(welcomeText())
userInput = sys.stdin.readline()
try:
    checkInput = inputChecker(userInput)
except Exception:
    print("Ha, ha, you don't even know what a number is!")

userInput = int(userInput)
while userInput != my_number:
    if userInput < my_number:
        print(userTooSmall())
        userInput = sys.stdin.readline()
        checkInput = inputChecker(userInput)
        userInput = int(userInput)
    else :
        print(userTooBig())
        userInput = sys.stdin.readline()
        checkInput = inputChecker(userInput)
        userInput = int(userInput)

print(goodByeText(my_number))
