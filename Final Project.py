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
        self.difficulty = "Medium" #difficulty level of the game
        self.guess_history = [] #this list is used for keeping track of guesses, right now its only displayed in hard mode
        self.max_attempts = 10 #this attribute sets the maximum number of attempts


    #this method checks to see if the number of attempts(guesses) has exceeded the threshold defined in init
    #this method takes no inputs but can end the game and returns either true or false to determine what to print
    def check_attempts(self):
        if self.attempt_num>= self.max_attempts: #if the attempts exceeds the max, then end the game and tell the user
            print(f"You have used all {self.max_attempts} attempts.")
            print(f"The correct answer was {self.answer}.")
            self.game_active = False
            return True
        return False


    #this method is takes a guess as input from the user. 
    #It prints hints to the user and can end the game when the right guess is found, this is medium difficulty
    def make_guess_medium_diff(self, guess):
        self.attempt_num+=1 #add one to the attempt counter
        self.guess_history.append(guess)
        if guess>self.answer: #if the guess was too large, prompt the user
            print("Too high")
            if not self.check_attempts(): #call check attempts to make sure that the user has not ran out of attempts
                print(f"Attempts remaining: {self.max_attempts - self.attempt_num}")
                print(" ") 

        elif guess<self.answer: #if the guess was too small, prompt the user
            print("Too low")
            if not self.check_attempts():#call check attempts to make sure that the user has not ran out of attempts
                print(f"Attempts remaining: {self.max_attempts - self.attempt_num}")
                print(" ")

        else: #if the guess was right, then end the game and print the appropriate messages
            print('Correct!')
            print(f"You've won the game. It took {self.attempt_num} attempts to guess the right number in medium difficulty mode.")
            self.game_active = False


    #this method is called when we want to make guesses in the easy difficulty mode
    #It prints hints to the user and can end the game when the right guess is found
    def make_guess_easy_diff(self, guess):
        self.attempt_num+=1 #add one to the attempt counter
        self.guess_history.append(guess)
        hint_ranges = {"very close": 5,"close": 10,"somewhat close": 20} #dictionary to correlate distance away with a prompt
        difference = abs(guess - self.answer) #get the absolute distance from the guess to the answer

        #use nested conditionals to give better hints to the user
        if guess > self.answer:#if the guess was too large, prompt the user
            print("Too high")
            if difference <= hint_ranges["very close"]:
                print("You are very close.")
            elif difference <= hint_ranges["close"]:
                print("You are close.")
            elif difference <= hint_ranges["somewhat close"]:
                print("You are somewhat close.")
            else:
                print("You are far away.")
            if not self.check_attempts(): #call check attempts to make sure that the user has not ran out of attempts
                print(f"Attempts remaining: {self.max_attempts - self.attempt_num}")     
            print(" ")

        elif guess < self.answer:#if the guess was too small, prompt the user
            print("Too low")
            if difference <= hint_ranges["very close"]:
                print("You are very close.")
            elif difference <= hint_ranges["close"]:
                print("You are close.")
            elif difference <= hint_ranges["somewhat close"]:
                print("You are somewhat close.")
            else:
                print("You are far away.")
            if not self.check_attempts(): #call check attempts to make sure that the user has not ran out of attempts
                print(f"Attempts remaining: {self.max_attempts - self.attempt_num}")
            print(" ")

        else: #if the guess was right, then end the game and print the appropriate messages
            print('Correct!')
            print(f"You've won the game. It took {self.attempt_num} attempts to guess the right number in easy mode.")
            self.game_active = False


    #this method is called when we want to make guesses in the hard difficulty mode
    #It prints hints to the user and can end the game when the right guess is found
    def make_guess_hard_diff(self, guess):
        self.attempt_num+=1 #add one to the attempt counter
        self.guess_history.append(guess)
        if guess !=self.answer: #if the guess was wrong, tell the user 
            print("Your guess was wrong, try again")
            print(f"You have tried: {self.guess_history}") #display the guesses you have tried already for hard mode
            if not self.check_attempts(): #call check attempts to make sure that the user has not ran out of attempts
                print(f"Attempts remaining: {self.max_attempts - self.attempt_num}")
            print(" ")

        else: #if the guess was right, then end the game and print the appropriate messages
            print('Correct!')
            print(f"You've won the game. It took {self.attempt_num} attempts to guess the right number in hard mode.")
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


#this function is for prompting the user to select the difficulty level and setting the difficulty attribute
#it takes no inputs and returns the string from the dictionary so it can be 
def select_difficulty():
    difficulty_options = {"1": "Easy","2": "Medium","3": "Hard"} #dictionary to hold the levels
    print("Select a difficulty level with the associated number")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Enter 1, 2, or 3: ") #prompt the user using input
    while choice not in difficulty_options: #if the choice is not in the dictionary then tell the user
        print("Invalid difficulty choice.")
        choice = input("Enter 1, 2, or 3: ")
    return difficulty_options[choice]


#this function contains the main loop that runs while the game is being played
#it takes no inputs and returns nothing
def main_run_game():
    input('Welcome to the Number Guessing Game! Press Enter to start the game.')
    this_game = game() # create a game object
    this_game.difficulty = select_difficulty() #call the select difficulty function to save it into the attribute
    while this_game.game_active: #continue to guess until the game ends
        guess = input("Enter a postive integer guess from 1 to 100: ")
        
        if validate_input(guess):
            guess2 =int(guess) #if the input is valid then we can convert into an int safely then pass to makeguess
            
            #select the right method to run based on the difficulty level selected by the user
            if this_game.difficulty =="Medium":
                this_game.make_guess_medium_diff(guess2)
            if this_game.difficulty =="Easy":
                this_game.make_guess_easy_diff(guess2)
            if this_game.difficulty =="Hard":
                this_game.make_guess_hard_diff(guess2)

        else:
            print("Your input is not valid, please try again.")


if __name__ == "__main__": #this code starts a game when your run the file
    main_run_game()