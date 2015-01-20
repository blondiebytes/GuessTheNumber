import random
import sys

#Guess the Number
# In this game, the user tries to guess the number thought up by the computer.
# The number is between 0 and 99.


#TO DO - Figure out a way to get rid of repeat-code


#FUNCTIONS

# Message: Welcoming Text
def welcomeText() :
    return "My name is The Number NINJA and I doubt you can guess " \
           "what\nnumber I\'m thinking of. It\'s between 0 and 99, " \
           "but what it is... \nyou\'ll never know. So go ahead, " \
           "take a guess... and fail."


# Message: if the user's guess is too big
def userTooBig() :
    randomNum = random.randrange(0,1000)
    if randomNum % 2 == 0 :
        return "Ha, ha. Think smaller! Or you will have no chance in figuring it out."
    else:
        return "Wrong wrong wrong! More isn't always better"

# Message: if the user's guess is too small
def userTooSmall() :
    randomNum = random.randrange(0,1000)
    if randomNum % 2 == 0:
       return "Ha, ha you are wrong! My number is way bigger than you think!"
    else:
        return "Nope!! You underestimate the power of my NUMBER!"

# Customized Type Checking
def isInputNum(user_input):
    return user_input.isdigit

def inputChecker(user_input):
    if not isInputNum(user_input):
        raise Exception("Invalid Input")

# Type Checker / Throw Exception(er)
def inputCheckerV2(userInput):
    try:
        userInput2 = int(userInput)
    except ValueError:
        print("Ha, ha, you don't even know what a number is! YOU LOSE and I shall be the Number Ninja"
              " forever! MUAHAHAHAHAHA! ")
        raise

# Message: Defeat Text
def goodByeText(my_num) :
    return "No, no, no! You figured out my secret number, %d! You must be some kind of mastermind \n" \
    "in the works. Grrr.... Go ahead. Tell all your friends you have beaten me, the Master of \n" \
    "All Numbers. You are now the new Number Ninja!"%(my_num)


ninja_number = random.randrange(0, 100)

# What we actually run....
print(welcomeText())
userInput = sys.stdin.readline()
inputCheckerV2(userInput)
userInput = int(userInput)
while userInput != ninja_number:
    if userInput < ninja_number:
        print(userTooSmall())
        userInput = sys.stdin.readline()
        inputCheckerV2(userInput)
        userInput = int(userInput)
    else :
        print(userTooBig())
        userInput = sys.stdin.readline()
        inputCheckerV2(userInput)
        userInput = int(userInput)

print(goodByeText(ninja_number))
