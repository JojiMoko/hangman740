# Importing the random library to choose a random word
import random
# Importing the list of words from another file
from milestone_2 import word_list

# Function to get a random word from the word list
word = random.choice(word_list)  # Pick a random word from the list
    
#Show the randomly selected word to the user
print("Here's a randomly selected word for you:", word)

#Ask for input
guess = input("Please enter a single letter: ")

#Verifying if input is valid (letter over word)
if len(guess) == 1 and guess.isalpha():
    #if input correct print "Good guess!"
    print("Good guess")
else:
    #if input invalid print "Invalid input, please try again"
    print("Oops! That is not a valid input.")