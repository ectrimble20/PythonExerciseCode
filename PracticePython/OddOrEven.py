# OddOrEven.py
"""
Ask the user for a number.  Depending on whether the number is even or odd, print out the appropriate message

Extras:
1 - if the number is a multiple of 4, print out a different message
2 - Ask the user for two numbers: one number to check and one number to divide by, if check
divides evenly into num, tell that to the user, if not print a different message
"""

num = int(input("Enter a number: "))
# num = int(num)  # still haven't figured out my obsession with not just wrapping input()

# check Extra #1 condition
if num % 4 == 0:
    print("You've entered a number that is divisible by 4")
else:
    if num % 2 == 0:
        print("You've entered an even number")
    else:
        print("You've entered an odd number")

# extra part two
n = int(input("Please enter another number: "))
# n = int(n)  # see
check = int(input("Enter a check number: "))
# check = int(check) # like, why Eric?  Just wrap the damn inputs

if n % check == 0:
    print("The numbers you've entered divide evenly")
else:
    print("The numbers you've entered do NOT divide evenly")

print("All done!")
