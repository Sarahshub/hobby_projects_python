# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

# Return selected or genereated word to guesss
def select_word(n):
    words = ['danish', 'intelligence', 'python', 'ballerina', 
         'meatballs', 'toast', 'sciencetist', 'british', 'halloween', 'misspell' ]
    word = words[n]
    amount = len(word)
    print(F'Your word have {amount} letters')
    print(' _ ' * amount)
    return word

# split word
def split_w(w):
    return [char for char in w]

# return the guessed letter if it is correct else return nothing 
def guess_letter(l, w):
    r = ''
    #word = split_w(w)
    for c in w:
        if c in l:
            r = r + str(c)
        else:
            r = r + ' _ '
    return r

# Check if given number is a number else generate number to select word        
def check_number(number):
    if (number > 10) or (number < 0) :
        print(F'Sorry {number} is not a valid number')
        new_number = random.randint(1,10)
        print(F'Your number is {new_number}')
        toguess = select_word(new_number)
        return toguess
    else:
        number = number - 1
        toguess = select_word(number)
        return toguess


# check if your guessed letter is wrong or right 
def trials(guess, guessedchars, toguess):
    if (guess not in guessedchars) and (guess in toguess):
        print('Good job!')
        return 0
    else:
        print('Nothing new..')
        return 1

    
#%%    

print('Welcome to hangman. Enter your name:')
name = input()
print(F'Hi {name}!')
print('Select a number between 1-10')
number = int(input())
toguess = str(check_number(number))
count = 5 
guessedchars = []
while (count > 0):
    print(F'You have {count} guesses left') 
    print('guess a letter')
    guess = str(input())
    count = count - trials(guess, guessedchars, toguess)
    guessedchars.append(guess)
    guesses = guess_letter(guessedchars, toguess)
    print(f'you have guessed {guessedchars}')
    print(guesses)
    if '_' not in guesses:
        print('You are a winner baby!')
        break
    if count == 0:
        print('Your man is dead. Game over!')
        break 
    
    





