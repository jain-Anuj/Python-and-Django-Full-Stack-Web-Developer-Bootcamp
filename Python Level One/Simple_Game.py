###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
code = digits[:3]
print(code)
print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")
print("Code has been generated! please guess a 3 digit number")
while True:
    guess = input("What is your guess? ")
    l = [int(x) for x in guess]
    if code[0] == l[0] and code[1] == l[1] and code[2] == l[2]:
        print("Perfect Match")
        break
    elif code[0] == l[0] or code[1] == l[1] or code[2] == l[2]:
        print("Match")
    else:
        flag = 0
        for n in l:
            for t in code:
                if n == t:
                    print("Close")
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 0:
            print(" Nope")























# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
