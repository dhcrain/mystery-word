# import my_functions
import random
import sys
import os

with open('/usr/share/dict/words') as opened_file:
    word_list = opened_file.readlines()


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def game():
    clear()

    def display_word():
        # clear()
        win_t = 0
        for letter in word:
            if letter in good_guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
                win_t += 1
        if win_t == 0:
            print("\n***** Winner *****")
            play_again()

    word = random.choice(word_list).upper()
    word = word.replace("\n", "")
    word = list(word)
    guess_max = 8
    bad_guesses = []
    good_guesses = []
    guess_count = 0
    print("Welcome to Mystery Word!\n"
          "You task is to guess the word in the blanks ({} letters long)\n".format(len(word)))
    while guess_count <= guess_max:
        print("".join(word) + ":remove after testing")

        display_word()

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
                print("\nYou Loose! The mystery word was {}".format(("".join(word))))
                play_again()


def play_again():
    if input("Do you want to play again? Y/n ").lower() != "n":
        game()
    else:
        sys.exit()

game()
