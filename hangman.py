import random
from milestone_2 import word_list

word = random.choice(word_list) 
print("Here's a randomly selected word for you:", word)

guess = input("Please enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input.")