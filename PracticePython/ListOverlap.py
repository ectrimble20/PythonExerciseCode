# ListOverlap.py
"""
Take two lists and write a program that returns a list that contains only the elements that are common between the
lists (without duplicates).  Make sure your program works on two lists of different sizes

I'm not doing the extra, I'll pull it from the solution and put it below so I can see how the single line is done.
I will however do the random list gen

On review of the "solution" there wasn't a good one liner for this.  At least not if you wanted to know what the lists
were prior to comparison.

I feel that this was a weak practice exercise
"""
import random

l_one = []
l_two = []
l_lgr = []
l_sml = []
l_unq = []

for _ in range(0, random.randrange(0, 20)):
    l_one.append(random.randrange(1, 100))
for _ in range(0, random.randrange(0, 20)):
    l_two.append(random.randrange(1, 100))
# for the above, I'd probably just use a function in the real world rather than rewrite

print("L One: ", l_one)
print("L Two: ", l_two)

if len(l_one) > len(l_two):
    l_lgr = l_one
    l_sml = l_two
else:
    l_lgr = l_two
    l_sml = l_one

for n in l_lgr:
    if n in l_sml:
        if n not in l_unq:  # ensure unique
            l_unq.append(n)

l_lgr.sort()
l_sml.sort()
l_unq.sort()

print("Here's our lists and our results:")
print("List Lgr: ", l_lgr)
print("List Sml: ", l_sml)
print("List Unq: ", l_unq)
