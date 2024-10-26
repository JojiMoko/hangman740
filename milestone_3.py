import random
from milestone_2 import word_list

secret_word = random.choice(word_list)

print("Welcome to Hangman! Try to guess the letters in the secret word.")

def check_guess(guess):
    guess = guess.lower()
    if guess in secret_word:
        print("Good guess, ",{guess}," is in the word")
    else:
        print({guess} ,"is not in the word, try again")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in secret_word:
                print(f"Good guess! '{guess}' is in the word.")
            else:
                print(f"Sorry, '{guess}' is not in the word. Try again.")
            
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()