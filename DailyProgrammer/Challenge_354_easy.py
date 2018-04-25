# Challenge_354_easy.py
"""
From Reddit r/dailyprogrammer

Given a number A, find the smallest possible value of B+C, if B*C = A. Here A, B, and C must all be positive integers.
It's okay to use brute force by checking every possible value of B and C. You don't need to handle inputs larger than
six digits. Post the return value for A = 345678 along with your solution.

Example solutions:
12 => 7
456 => 43
4567 => 4568
12345 => 838
"""
from time import time
from math import sqrt
from math import ceil

# we'll need to solve for 345678 to complete the challenge


def get_lowest_factor(num_in):
    lowest = num_in + 1             # we know our lowest start point is num in + 1
    rng = ceil(sqrt(num_in))        # we can eliminate a large part of the range by getting the sqrt of the num in
    for i in range(1, rng):         # loop on our range
        if num_in % i == 0:         # if num_in % N == 0, the number is evenly divisible
            p = num_in / i          # set a check value to num_in / N
            if i + p < lowest:      # check if this value is lower than our current lowest
                lowest = i + p      # if so, assign it as the new lowest value
    return int(lowest)              # return the absolute lowest value


l = [12, 456, 4567, 12345, 345678, 1234567, 1234567891011]  # for the optional, too big to eff do with my knowledge

for x in l:
    s = time()
    n = get_lowest_factor(x)
    e = time()
    ex = str(e - s) + "s"
    print("Factor", x, "=", n, "ex:", ex)

"""
Return from this run

Factor 12 = 7 ex: 0.0s
Factor 456 = 43 ex: 0.0s
Factor 4567 = 4568 ex: 0.0s
Factor 12345 = 838 ex: 0.0s
Factor 345678 = 3491 ex: 0.0s
Factor 1234567 = 9848 ex: 0.0s
Factor 1234567891011 = 2544788 ex: 0.2590627670288086s
"""