import random
from milestone_2 import word_list

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.secret_word = random.choice(word_list).lower()
        self.num_lives = num_lives
        self.guessed_word = ["_"for _ in self.secret_word]
        self.guessed_letter = []
        self.remaining_letters = len(set(self.secret_word))
        
    def check_guess(self, guess):
        if guess in self.secret_word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            self.update_guessed_word(guess)
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
            
    def update_guessed_word(self, guess):
        for index, letter in enumerate(self.secret_word):
            if letter == guess:
                self.guessed_word[index] = guess
            self.remaining_letters = len(set(self.secret_word) - set(self.guessed_letter))
            
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").strip().lower()
            if self.is_valid_guess(guess):
                self.guessed_letter.append(guess)
                return guess
            else:
                print("Invalid input. Please enter a single letter.")
                
    def is_valid_guess(self, guess):
        return len(guess) == 1 and guess.isalpha()
    
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print("You've lost")
            break
        elif game.remaining_letters == 0:
            print("Congratulations! You won the game!")
            break
        else:
            guess = game.ask_for_input()
            game.check_guess(guess)
            
if __name__ == "__main__":
    play_game(word_list)

            
                
                
        

    