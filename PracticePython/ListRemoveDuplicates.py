# ListRemoveDuplicates.py
"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
"""


def remove_duplicates_list(in_list):
    tmp_list = []
    for n in in_list:
        if n not in tmp_list:
            tmp_list.append(n)
    return tmp_list


def remove_duplicates_sets(in_list):
    return list(set(in_list))


a = [1, 1, 3, 4, 5, 5, 6, 6, 6, 7, 2, 3, 5, 1, 10, 2, 4]
b = [4, 2, 6, 1, 7, 7, 1, 20, 12, 20, 0, 0, 1, 5, 2, 2, 3, 1]

print("A List: ", a)
print("B List: ", b)

a1 = remove_duplicates_list(a)
b1 = remove_duplicates_list(b)

print("A1: ", a1)
print("B1: ", b1)

a2 = remove_duplicates_sets(a)
b2 = remove_duplicates_sets(b)

print("A2: ", a2)
print("B2: ", b2)
