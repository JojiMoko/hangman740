import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """Initialize the Hangman game with a random word and game settings."""
        self.word_list = word_list 
        self.word = random.choice(self.word_list) 
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess, ",{guess}," is in the word")
            
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left")
            
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").strip().lower()
            
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You've already tried that letter")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

if __name__ == "__main__":
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    game = Hangman(words)
    print(f"The word to guess: {' '.join(game.word_guessed)}")
    print(f"Unique letters to guess: {game.num_letters}")
    print(f"Starting lives: {game.num_lives}")
    
game.ask_for_input()