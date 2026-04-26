#Zach Mosier CMPSC 132 Final Project
#this code is a terminal based number guessing game
#see the README and report for more detailed descriptions

import random


#this class defines game objects which represent a single game with a user
class game:
    def __init__(self):
        self.attempt_num = 0 #start off with zero guesses
        self.answer = random.randint(1,100) #pick a random number that will be the solution to the game
        self.game_active = True #game is initially active

    
    #this method is takes a guess as input from the user. It prints hints to the user and can end the game when the right guess is found
    def make_guess(self, guess):
        self.attempt_num+=1 #add one to the attempt counter

        if guess>self.answer: #if the guess was too large, prompt the user
            print("Too high")
            print(" ")
        elif guess<self.answer: #if the guess was too small, prompt the user
            print('Too low')
            print(" ")
        else: #if the guess was right, then end the game and print the appropriate messages
            print('Correct!')
            print(f"You've won the game. It took {self.attempt_num} attempts to guess the right number.")
            self.game_active = False


#this function handles all the input validations. It takes a guess as input and returns either true or false
def validate_input(guess):
    if not guess.isdigit(): #use built in method to filter out things like negatives
        return False
    try: #if the int conversion fails then we want to return false so the user can be prompted
        guess = int(guess)
    except ValueError:
        return False

    if guess <=0: #make sure that the guess is in the specified range
        return False
    elif guess >= 1 and guess <= 100: #only return true if all the above conditions pass and it's in the right range
        return True
    else: #redundant catch all
        return False
    

#this function contains the main loop that runs while the game is being played
#it takes no inputs and returns nothing
def main_run_game():
    input('Welcome to the Number Guessing Game! Press Enter to start the game.')
    this_game = game() # create a game object

    while this_game.game_active: #continue to guess until the game ends
        guess = input("Enter a postive integer guess from 1 to 100: ")
        
        if validate_input(guess):
            guess2 =int(guess) #if the input is valid then we can convert into an int safely then pass to makeguess
            this_game.make_guess(guess2)
        else:
            print("Your input is not valid, please try again.")


if __name__ == "__main__": #this code starts a game when your run the file
    main_run_game()