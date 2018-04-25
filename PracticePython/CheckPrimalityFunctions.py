# CheckPrimalityFunctions.py
"""
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime
number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this
opportunity to practice using functions, described below.
"""


user_input = int(input("Enter a number:"))
is_prime = True

for n in range(2, user_input):
    if user_input % n == 0:
        is_prime = False
        break

if is_prime:
    print("You entered", user_input, "which is a prime number")
else:
    print("You entered", user_input, "which is not a prime number")
