# ListLessThanTen.py
"""
Take a list and write a program that prints out all the elements of the list that are less than 5

Extras:
1 - instead of printing the elements one by one, make a new list that has all the elements less than 5 from the list
2 - Write this in one line of python
3 - Ask the user for a number and return a list that contains only elements from the orig list that are smaller
than the number given by the user
"""

# Note: Going to do this in chunks for each task

# fib sequence
o_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("Elements that are less than 5, individually:")
for i in o_list:
    if i < 5:
        print(i, "is less than 5")

print("\n\n")
print("New List with elements less than 5:")
n_list = []
for i in o_list:
    if i < 5:
        n_list.append(i)
print(n_list)
print("\n\n")

print("Done in one line:")
print("[i for i in o_list if i < 5]")
print([i for i in o_list if i < 5])

print("Ask user for input and print list of less than input:")
num = input("Please enter a number: ")
num = int(num)
print([i for i in o_list if i < num])

print("\n\nAll done!")
