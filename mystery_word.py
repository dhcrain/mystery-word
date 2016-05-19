# import my_functions
import random

with open('/usr/share/dict/words') as opened_file:
    word_list = opened_file.readlines()

# print instructions
word = random.choice(word_list).upper()
word = word.replace("\n", "")
word = list(word)
guess_max = 8
guess_count = 0
bad_guesses = []
good_guesses = []

while guess_count <= guess_max:
    print("".join(word) + ":remove after testing")

    for letter in word:
        if letter in good_guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
        if letter not in word:
            print("win")
            break

    # if len(good_guesses) == len(word):
    #     print("You win!")
    #     break

    print("\nBad Guesses [{}/{}]".format(guess_count, guess_max))
    for letter in bad_guesses:
        if letter in bad_guesses:
            print(letter, end=" ")

    letter = input("\n" + "_" * 40 + "\nGuess a letter: ").upper()
    if len(letter) != 1:
        print("You can only guess one letter at a time!\n")
    elif letter in bad_guesses or letter in good_guesses:
        print("You already guessed that one!\n")
    elif not letter.isalpha():
        print("That's not a letter!\n")
    else:
        if letter in word:
            print("Good Guess!\n")
            good_guesses.append(letter)
        else:
            print("Bad Guess!\n")
            bad_guesses.append(letter)
            guess_count += 1
        if guess_count == guess_max:
            print("You Loose! The mystery word was {}".format(("".join(word))))
            break

