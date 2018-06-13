# ElementSearch.py
import random
"""
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to
largest) and another number. The function decides whether or not the given number is inside the list and
returns (then prints) an appropriate boolean.

Extras:

Use binary search.
"""

elements = random.randint(40, 100)
e_list = list(set([random.randint(0, 100) for n in range(0, elements)]))
"""
e_list = []
for _ in range(0, elements):
    n = random.randint(0, 100)
    e_list.append(n)
e_list = list(set(e_list))  # convert and sort
"""
e_list.sort()  # make sure it's sorted

s_element = random.randint(0, len(e_list))

# print("Random List:", e_list)
print("Random List: {}".format(e_list))
# print("Random element:", s_element, "Value: ", e_list[s_element])
print("Random element: {} => Value: {}".format(s_element, e_list[s_element]))


def binary_search(search_for: int, search_in: list) -> object:
    """
    This is a binary search function for a list of sorted integer values.  It follows the following steps to quickly
    search the list in a half-interval search pattern.

    Step 1:  Set Left-Index to 0, Set Right-Index to search_in length minus 1 (n-1)
    Step 2:  Check if Left-Index is greater than Right-Index, if so, return -1, not found in the list
    Step 3:  Set Middle-Index to the floor of Left-Index + Right-Index divided by 2 ((L+R)//2)
    Step 4:  If Value At Middle-Index is less than search Value, set Left-Index to Middle-Index + 1, Go to Step 2
    Step 5:  If Value at Middle-Index is greater than search Value, set Right-Index to Middle-Index - 1, Go to Step 2
    Step 6:  If Value at Middle-Index equals search Value, return Middle-Index

    :param search_for: int we're searching for
    :param search_in: list of sorted ints to search
    :return: int index (-1 if not found)
    """
    step = 0
    l = 0
    r = len(search_in) - 1
    while True:
        # print("Debug:step:L:R:", step, l, r)
        step += 1
        if l > r:
            print("l > r, no result")
            return -1
        m = (l + r) // 2
        # print("M::", m)
        # Start binary search
        if search_in[m] == search_for:
            return m
        if search_in[m] < search_for:
            l = m + 1
        else:
            r = m - 1


res = binary_search(s_element, e_list)
if res is not -1:
    print("Found {} at index {}".format(s_element, res))
    # print("Found", s_element, "at index", res)
else:
    print("Did not find {} in the list".format(s_element))
    # print("Did not find", s_element, "in the list")
