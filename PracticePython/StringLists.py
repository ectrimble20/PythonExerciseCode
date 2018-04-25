# StringLists.py
"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

user_input = input("Enter a string that is more than 5 char:")
user_input = str(user_input)
if len(user_input) < 5:
    print("You didn't follow my instructions >:(")
    quit()

l_rev = list(user_input)
l_rev.reverse()
rev = ''.join(l_rev)
print(rev)


if rev.lower() == user_input.lower():
    print("You've entered a Palindrome! good job nerd")
else:
    print("You didn't enter a palindrome, good job not being a nerd.... NERD!! haha you lose either way")
