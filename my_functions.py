
def intro():
    print("")

def turn():
    letter = input("Guess a letter: \n"
                   "You have used {} out of {} guesses"
                   .format(guess_count, guess_max)).upper()
    print("_ " * len(word))