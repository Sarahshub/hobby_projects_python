# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:28:31 2022

@author: 44791
"""

'''First exercise in python workout 'Number guessing game'. 
Instructions:
    most be in a function "guessing_game" that doesn't take any arguments.
    Function choose number(1-100) to guess for user.
    User can give guesses and gets feedback 
    n > x too high
    n < x too low 
    n == x just right 
    when n == x the program exits 
    
    '''
 
import random     

def guessing_numbers():
    secret_number = random.randint(1, 100)
    print('Hi and welcome to the guessing game.')
    guessed = 0
    print('Guess a number between 1-100')
    while guessed != secret_number:
        guess = input()
        guess = int(guess)
        if guess == secret_number:
            print('That is just right! You won!')
            guessed = guess
            break
        if guess < secret_number:
            print('Too low my friend.. Shoot for the stars!')
            guessed = guess
        if guess > secret_number:
            print('Too high.. try again..')
            guessed = guess
    