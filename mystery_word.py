import my_functions
import random

with open('/usr/share/dict/words') as opened_file:
    word_list = opened_file.readlines()

word = random.choice(word_list)
print("word: " + word)
guess_max = 8 + len(word)
guess_count = 0
guesses = []
letter = input("Guess a letter: ")
print(" _" * len(word))

if letter in word:


# print instructions
# tell user how many letters are in the word
# Let the user know if their guess appears in the computer's word.
# Display the partially guessed word
# allow 8 guesses, only loose guess when there is a miss
# if user runs out of guesses show the word
# if guess same letter tell them
