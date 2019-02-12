# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 14:30:45 2019

@author: Bruno
"""

#Guess the number game

import random

number = random.randint(1,9)
print('I am thinking of a number between 1 and 9.')

guessesTaken = 0
sw = 0

while sw == 0:
    print('Take a guess.')
    guess = input()
    guess = int (guess)
    
    guessesTaken = guessesTaken +1
    
    if guess < number:
        print('Your guess is too low.')
        
    if guess > number:
        print ('Your guess is too high.')
        
    if guess == number:
        break
        sw = 1
    e = input()
    if e == ('exit'):
        print('game over')
        break
    
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job! you guessed my number in '+guessesTaken+' guesses!')
            