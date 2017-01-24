import random
import string

letter = random.choice(string.ascii_lowercase)
guess_count = 0

while True:
    letter_guess = raw_input('Guess a letter ')
    guess_count = guess_count + 1
    if letter_guess < letter:
         print 'Higher'
         continue
    if letter_guess > letter:
         print 'Lower'
         continue
    elif letter_guess == letter:
         print 'Correct answer!'
    break
    
         
    
        