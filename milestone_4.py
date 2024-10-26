import random
from milestone_2 import word_list

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list 
        self.secret_word = random.choice(self.word_list) 
        self.guessed_word = ["_" for _ in self.secret_word]
        self.remaining_letters = len(set(self.secret_word))
        self.lives_left = num_lives
        self.guessed_letters = []
    
    def _update_guessed_word(self, guess):
        for index, letter in enumerate(self.secret_word):
            if letter == guess:
                self.guessed_word[index] = guess
        self.remaining_letters -= 1

    def _handle_correct_guess(self, guess):
        print(f"Good guess! The letter '{guess}' is in the word.")
        self._update_guessed_word(guess)

    def _handle_incorrect_guess(self, guess):
        self.lives_left -= 1
        print(f"Sorry, '{guess}' is not in the word. Try again.")
        print(f"You have {self.lives_left} lives left.")

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.secret_word:
            self._handle_correct_guess(guess)
        else:
            self._handle_incorrect_guess(guess)

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").strip().lower()
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid input. Please enter a single letter.")
            elif guess in self.guessed_letters:
                print("You've already tried that letter.")
            else:
                self.guessed_letters.append(guess)
                self.check_guess(guess)
                break

if __name__ == "__main__":
    game = Hangman(word_list)
    
    print(f"The word to guess: {' '.join(game.guessed_word)}")
    print(f"Unique letters to guess: {game.remaining_letters}")
    print(f"Starting lives: {game.lives_left}")
    
    while game.lives_left > 0 and '_' in game.guessed_word:
        game.ask_for_input()
        print(f"Current guess: {' '.join(game.guessed_word)}")
