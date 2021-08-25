from random import randint

def rangevalue() :
    """Sets up the range of value of where you would guess the number"""
    while True:
        try:
            val_range = [int(input("Enter low value: ")), int(input("Enter high value: "))]
            if val_range[0] < val_range[1]:
                return val_range
            else:
                print("low value should be lower than high value")
        except ValueError:
            print("Enter an integer.")


def guess_number():
    """Adding or not adding limits to the guesses"""
    while True:  # Finds if the user wants a guess limit
        guesses_number = input("Add limit to your guesses? | 'yes' or 'no' |: ")
        if guesses_number == "yes" or guesses_number == "no":
            if guesses_number == "no":
                return None
            while True:
                try:
                    guesses_number = int(input("Number of Guesses: "))
                    if guesses_number > 0:
                        return guesses_number
                    else:
                        print("Number should be greater than 0")
                except ValueError:
                    print("Enter an integer")
        else:
            print("Enter 'yes' or 'no' ")



def setup():
    """Sets up the game parameters"""
    val_range = rangevalue()
    guesses_number = guess_number()
    return val_range, guesses_number

def guessing(randomnum: int):
    """As the player is guessing"""
    while True:
        try:
            guess = int(input("What is your guess? : "))
            if guess == randomnum:
                print("Great Job")
                return True
            elif guess > randomnum:
                print("The number is lower.")
                return False
            elif guess < randomnum:
                print("The number is higher.")
                return False
        except ValueError:
            print("Enter an integer ")


def reset() :
    """Asks if player want to quit or continue the game before"""
    while True:  # Checks if the user wants to quit the game
        ending = input("Do you want to continue? | 'yes' or 'no' |: ")
        if ending == "no" or ending == "yes":
            if ending == "no":
                quit()
            else:
                break

val_range, guesses_number = setup()
while True:
    randomnum = randint(val_range[0], val_range[1])
    if guesses_number is None:
        while True:
            if guessing(randomnum):
                break
    else:
        for _ in range(guesses_number):
            right = guessing(randomnum)
            if right:
                break
        else:
            print("Guess limit reached")
    if reset():
        val_range, guesses_number = setup()