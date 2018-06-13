# GuessingGameOne.py
"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
whether they guessed too low, too high, or exactly right.

Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.

I didn't bother with the first extra, seemed kinda pointless as it would just be an extra loop to implement this
"""

import random


r_num = random.randint(0, 9)
guesses = 0
guess_text = "guesses"
while True:
    u_in = int(input("Enter your guess:"))
    # u_in = int(u_in)
    guesses += 1
    if u_in == r_num:
        if guesses == 1:
            print("Nice, guessed it on the first try!")
            guess_text = "guess"
            break
        else:
            print("You got it!")
            break
    else:
        if u_in > r_num:
            print("Guessed too high")
        else:
            print("Guessed too low")

print("It took", guesses, guess_text)
quit()
