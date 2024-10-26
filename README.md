# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


#HANGMAN PROJECT 0.1

##HANGMAN PROJECT
adding milestone by milestone

## Milestone_2
contians 2 files as i've made separated word list from milestone_2.py (confusingly named but: milestone_2.py = word_list ; hangman.py = actual code for milestone_2.py)
1. import method to import from milestone_2.py (word_list) 
2. random.choice method to choose rnadom word, assigned to variable word / test if prints out random
3. input request, len = 1 and isalpha criteria
4. check if rule above is met, if not print invalid input

## Milestone_3
Introducing while loop
### 1st = import list for word_list
1. while = true 
2. adding user input variable guess
3. check if input is letter (isalpha)
4. in the loop check if conditions are met (if input is valid or not)
5. check code : ask_for_input()

## Milestone_4
defining __init__ method
class hangman creation  with init method and passing word_list and num_lives as params, param for lives = 5
1. word: initilizing picking random word (at random from word_list)
2. word_guessed: (list) and if guessed to replace _ with letter)
3. num_letters (int) remaining unguessed unique letteres
4. num_lives: int = 5
5. word_list: list of words (pulled from list)
6. list_of_guesses: list = tried already (initial empty)

## Milestone_5 
Continuing milestone_4.py 
1. setting play function that takes word_list as param
2. instance Hangman set variabl game = hangman (word list , numb lives)
3. passing word_list n num_lives as arguments to game object
4. while loop added to check if num_lives is 0, if so to print "you lost", if greater than 0 to ask for input (ask_for_input ) and if num_lives is not to print "You won the game"
5. called play_game / tested.

## Whoever reads this - Im sorry for the sloppy README.md , its literally my first one, feel free to add comments where needed. Kept it as simple as possible.
