import numpy as np
import random
from collections import Counter

help_text = """The aim of Mastermind is to correctly guess the secret four-pin pattern
made by the computer. Both the location and the colour of each pin must be correct. 
The pattern could be something like 'red green blue black' or 'red blue yellow blue', for example. 
After each guess, the computer will tell you how many pins you have which are:
-- in the correct location and have the correct colour
-- have the correct colour but the location is wrong
-- are not the correct colour.
However, it will not tell you *which* pins are correct and which are wrong. You may then guess again,
and the process repeats until you crack the code.

EXAMPLE:
    
Imagine the secret pattern is 'red orange black blue'.
If your guess is 'red green orange black', then the response will be:
-- 1 pin of the right colour AND in the right place
-- 2 pins of the right colour but in the wrong place
-- 1 pin of the wrong colour.

If your guess is 'red black blue blue', then the response will be:
-- 2 pins of the right colour AND in the right place
-- 1 pin of the right colour but in the wrong place
-- 1 pin of the wrong colour.
i.e. the two 'blue' guesses are treated differently.
"""

colours = ['red', 'yellow', 'green', 'blue', 'orange', 'purple', 'black', 'white']
colours1 = colours

print "Thanks for playing Mastermind with me! The colours in the game are: "
for c in colours:
    print c

#random.shuffle(colours1)
#pattern = colours1[:4]
pattern = [random.choice(colours) for i in xrange(4)]

print """ \nI have chosen a pattern of four coloured pins (colours may be repeated.)
Please make your first guess. Your input must be a single line of four words separated by spaces.
E.g. red yellow green blue
If you need help at any point then please type HELP. If you want to quit the game, please type
EXIT. Good luck!"""

solve = 0
guess = []
num_guesses = 0

while solve == 0:
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
    
        elif guess_str == 'HELP' or guess_str == 'help':
            print help_text
            continue
        
        elif guess_str == 'EXIT' or guess_str == 'exit':
            print "Goodbye!"
            break
        
        guess = str.split(guess_str)
        
        pat_ctr = Counter(pattern)    # count for each colour in pattern
        white_ctr = 0   # right colour wrong location
        red_ctr = 0    # right colour right location
        none_ctr = 0   # wrong colour
        
        test_list = []
        
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
                    pat_ctr[guess[i]] -= 1
                else:
                    test_list.append(i)
            
            for i in test_list:
                    
                if guess[i] != pattern[i] and guess[i] in pattern:
                    if pat_ctr[guess[i]] > 0:
                        white_ctr += 1
                        pat_ctr[guess[i]] -= 1
                    else:
                        none_ctr += 1
                    
                else:
                    none_ctr += 1
            
            num_guesses += 1
            
            if red_ctr == 4:
                continue
            else:
                print """\nYou have %g pin(s) of the right colour AND in the right place,
                        %g pin(s) of the right colour but in the wrong place,
                        and %g pin(s) of the wrong colour.""" % (red_ctr, white_ctr, none_ctr)
                print "Please guess again."
    
    if guess == pattern:
        solve = 1
    else:
        break
    
if solve == 1:
    print "\nYou cracked the code! My pattern was indeed:"
    print pattern
    
    if num_guesses == 1:
        print "You solved it in one guess...are you sure you didn't cheat?"
    else:
        print "It took you %d guesses" % num_guesses
        print "Nice job!"