import random
import sys
import os

with open('/usr/share/dict/words') as opened_file:
    word_list = list(opened_file.readlines())

easy_min = 5
easy_max = 7
med_min = 6
med_max = 10
hard_min = 10
hard_max = 99

# make 3 lists
easy_list = []
med_list = []
hard_list = []
for words in word_list:
    # PyCharm tells me I can simplify this comparison, but I cant seem to get it work; if min <= len(words) >= max:
    # easy list
    if len(words) >= easy_min and len(words) <= easy_max:
        easy_list.append(words.replace("\n", ""))
    # med list
    if len(words) >= med_min and len(words) <= med_max:
        med_list.append(words.replace("\n", ""))
    # hard list
    if len(words) >= hard_min and len(words) <= hard_max:
        hard_list.append(words.replace("\n", ""))


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def play_again():
    if input("Do you want to play again? Y/n ").lower() != "n":
        game()
    else:
        sys.exit()


def welcome():
    pass


def rand_word(level_word_list):
    word = random.choice(level_word_list).upper()
    word = word.replace("\n", "")
    word = list(word)
    return word


def game():

    # Get a level choice
    print("Welcome to Mystery Word!\n"
          "Choose the game level:\n"
          "1. Easy   - Words 4-6 letters long\n"
          "2. Medium - Words 6-10 letters long\n"
          "3. Hard   - Words longer than 10 letters")
    level = input("Choose 1, 2, 3: ")

    if level == "1":
        word = rand_word(easy_list)
    elif level == "2":
        word = rand_word(med_list)
    elif level == "3":
        word = rand_word(hard_list)
    else:
        print("Must choose 1, 2, or 3 please.\n")
        play_again()

    def display_word():
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

    guess_max = 8
    bad_guesses = []
    good_guesses = []
    guess_count = 0

    while guess_count <= guess_max:

        # print(str(word) + ":remove after testing")

        print("\nYou task is to guess the word in the blanks.")
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

game()
