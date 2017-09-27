import numpy as np
import random

colours = ['red', 'yellow', 'green', 'blue', 'orange', 'purple', 'black', 'white']
colours1 = colours

print "Thanks for playing Mastermind with me! The colours in the game are: "
for c in colours:
    print c

random.shuffle(colours1)
pattern = colours1[:4]

print """ \nI have chosen a pattern of four different-coloured pins. Please make your first guess.
Your input must be a single line of four words separated by spaces.
E.g. red yellow green blue
If you need help at any point then please type "HELP" below."""

guess = []
num_guesses = 0

while guess != pattern:
    guess_str = raw_input()

    # for debugging:
    if guess_str == 'pattern':
        print pattern
        print "\nHey, no cheating!"
        continue

    if guess_str == 'colours':
        print "\nThe colours in the game are: "
        for i in colours:
            print i
        continue

    elif guess_str == 'HELP':
        print "\nHelp guide coming soon...."
        continue
    
    guess = str.split(guess_str)

    white_ctr = 0   # right colour wrong location
    red_ctr = 0    # right colour right location
    none_ctr = 0   # wrong colour
    
    wrong = []
    for i in guess:
        if i not in colours:
            wrong.append(i)
    
    if wrong:
        print "\nThe following are not colours in the game: "
        for i in wrong:
            print i
        print "\nPlease try again. If you need to see a list of allowed colours, please type colours."
        
    else:
        for i in xrange(len(guess)):
            
            if guess[i] == pattern[i]:
                red_ctr += 1
    
            elif guess[i] != pattern[i] and guess[i] in pattern:
                white_ctr += 1
                
            else:
                none_ctr += 1
        
        num_guesses += 1
        
        if red_ctr == 4:
            continue
        else:
            print """\nYou have %g pin(s) of the right colour AND the right place,
                    %g pin(s) of the right colour but in the wrong place,
                    and %g pin(s) that are not the right colour.""" % (red_ctr, white_ctr, none_ctr)
            print "Please guess again."

print "\nYou cracked the code! My pattern was indeed:"
print pattern

if num_guesses == 1:
    print "You solved it in one guess...are you sure you didn't cheat?"
else:
    print "It took you %d guesses" % num_guesses
    print "Nice job!"
