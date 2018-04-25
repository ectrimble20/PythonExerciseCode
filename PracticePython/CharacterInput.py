# CharacterInput.py
"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year they will turn 100

Extra:
1 - add-on to the previous task by asking the user to enter a number and printing out the message
from the previous task by N times
2 - from task 1, print the message on a new line
"""

name = input("Welcome! Please enter you name:")
name = str(name)
age = input("Thanks " + name + ", say... how old are you? ")
age = int(age)

year_100 = (2018 - age) + 100
year_99 = year_100 - 1
msg = "Wow, well depending on what month you were born, you'll be 100 in", year_100, "or", year_99
print(msg)


repeat = input("Hey, enter a number between 1-5, or w/e it's a surprise what I'm going to do: ")
repeat = int(repeat)
print(msg * repeat)
print("Pretty neat huh?  Okay, I'm going to do the same thing but on diff lines now")
for n in range(repeat):
    print(msg)

print("All done!")
