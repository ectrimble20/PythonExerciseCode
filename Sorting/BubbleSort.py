# BubbleSort.py
import random
from time import time


def bubble_sort(in_list):
    while True:
        swapped = False
        for i in range(1, len(in_list)):
            if in_list[i-1] > in_list[i]:
                in_list[i], in_list[i-1] = in_list[i-1], in_list[i]
                swapped = True
        if not swapped:
            break
    return in_list


elements = random.randint(10, 40)
e_list = []
for _ in range(0, elements):
    n = random.randint(0, 100000)
    e_list.append(n)
d_list = e_list.copy()
c_list = e_list.copy()
p_list = e_list.copy()

print("Elements:", len(e_list))
print("Orig List:", e_list)
s = time()
print("Sorted:   ", bubble_sort(d_list))
e = time()
print("Time My Bubble sort:", e-s)

ss = time()
c_list.sort()
es = time()
print("Built-In sort time:", es-ss)
print("Sorted:   ", c_list)
