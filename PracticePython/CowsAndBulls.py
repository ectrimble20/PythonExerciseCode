# CowsAndBulls.py
import random
"""
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user
guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in
the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes
throughout the game and tell the user at the end.
"""
num = []
for _ in range(0, 4):
    n = random.randint(0, 9)
    num.append(str(n))

print("|||||||||||||||||||||||||||||||||||||||||||||||")
print("||||COWS|||||||||||||||||||||||||||||||||||||||")
print("||||||||||AND||||||||||||||||||||||||||||||||||")
print("||||||||||||||||BULLS||||||||||||||||||||||||||")
print("|||||||||||||||||||||||||||||||||||||||||||||||")

print("Debug:", num)

won = False
guesses = 0
while not won:
    u = input("Enter your 4 digit guess: ")
    u = str(u)
    if len(u) < 4 or len(u) > 4:
        print("Your guess must be 4 digits")
        continue
    if not u.isnumeric():
        print("Your guess must only have number")
        continue
    guesses += 1
    cow_str = "cow"
    bull_str = "bull"
    cow = 0
    bull = 0
    for c in u:
        if c in num:
            if u.index(c) == num.index(c):
                cow += 1
            else:
                bull += 1
    if cow > 1:
        cow_str = "cows"
    if bull > 1:
        bull_str = "bulls"
    if cow == 4:
        print("You got it right, good job!  It took you", guesses, "guesses")
        won = True
    else:
        print(cow, cow_str, ",", bull, bull_str)
