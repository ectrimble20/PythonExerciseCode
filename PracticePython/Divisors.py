# Divisors.py
"""
Create a program that asks the user for a number then prints out a list of all the divisors of that number
...divisor is a number that divides evenly into another number, ex 13 is a divisor of 26 because 26 % 13 == 0
"""

num = input("Enter a number to get it's divisors: ")
num = int(num)

l = []
# for n in range(1, num):  -- we need to add 1 to the range in order to ensure we check itself
for n in range(1, num+1):
    if num % n == 0:
        l.append(n)

print("Divisors of", num, "are", l)


print("One liner attempt:")
print("[n for n in range(1, num+1) if num % n == 0]")
print([n for n in range(1, num+1) if num % n == 0])
