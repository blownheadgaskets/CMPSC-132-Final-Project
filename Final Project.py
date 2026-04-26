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
        elif guess<self.answer: #if the guess was too small, prompt the user
            print('Too low')
        else: #if the guess was right, then end the game and print the appropriate messages
            print('Correct!')
            print(f"You've won the game. It took {self.attempt_num} attempts to guess the right number.")
            self.game_active = False

def validate_input():
    pass

def main_run_game():
    pass
