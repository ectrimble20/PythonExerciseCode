# ListEnds.py
"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of
only the first and last elements of the given list. For practice, write this code inside a function.

Could use the deque from collections to get popleft() which would do the [0] index for us
"""


def first_and_last(l_ist):
    n_list = list()
    n_list.append(l_ist[0])
    n_list.append(l_ist.pop())
    return n_list


a = [5, 10, 15, 20, 25]
c_a = a.copy()
b = first_and_last(c_a)

print("A:", a)
print("B:", b)
