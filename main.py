import random

def setNum(bound1, bound2):
    """This wil set the answer to a random number"""
    number = random.randint(bound1, bound2)
    return number

def beginGame():
    """This will run the main game"""
    print("Hi! We are going to play a game. Please enter the lowest and highest number to play with.")
    lower = input("Please enter the low number. ")
    upper = input("Please enter the high number. ")
    upper = int(upper)
    lower = int(lower)
    global answer
    answer = setNum(lower, upper)
    print("Deciding a number...")
    print("Got it!")
    guess()

def check(userNum: int):
    """This will compare the user entered number to the set answer"""
    userGuess = userNum
    userGuess = int(userGuess)
    userNum
    if userGuess > answer :
        print("Too High! Guess Again. ")
        guess()
    elif userGuess < answer :
        print("Too low! Guess Again. ")
        guess()
    elif userGuess == answer:
        print("You got it! Great job. ")
        quit()

def guess():
    """This will get the user to guess a number"""
    global userGuess
    userGuess = input("Please enter your guess!")
    int(userGuess)
    print("You entered: " + userGuess + ", is this correct? ")
    global confirmation
    confirmation = input("Enter Y for yes, or N for no. ")
    confirm(confirmation)

def confirm(entry):
    """this confirms the Y or N entry"""
    if entry == "Y":
        check(userGuess)
    elif entry == "N":
        print("Please re-enter your number. ")
        guess()
    else:
        print("Sorry, we couldn't understand that. Please enter a Y or an N. ")
        global newConfirmation
        newConfirmation = input("Please try again. ")
        confirm(newConfirmation)

beginGame()