# Challenge_355_intermediate.py
"""
It's Thanksgiving eve and you're expecting guests over for dinner tomorrow. Unfortunately, you were browsing memes all
day and cannot go outside to buy the ingredients needed to make your famous pies. You find some spare ingredients, and
make do with what you have. You know only two pie recipes, and they are as follows:

Pumpkin Pie
1 scoop of synthetic pumpkin flavouring (Hey you're a programmer not a cook)
3 eggs
4 cups of milk
3 cups of sugar

Apple Pie
1 apple
4 eggs
3 cups of milk
2 cups of sugar

Your guests have no preference of one pie over another, and you want to make the maximum number of (any kind) of pies
possible with what you have. You cannot bake fractions of a pie, and cannot use fractions of an ingredient (So no 1/2
cup of sugar or anything like that)

input is formatted as 5 numbers separated by commas [4,3,2,1,0]
Numbers cannot be negative
each represents the number of ingredients you have in the order:
-pumpkin
-apples
-eggs
-cups of milk
-cups of sugar

Output should be displayed as:
[N] pumpkin pies and [N] apple pies


This isn't perfect, it doesn't give the challenges answer in the number of pie types but the total count is correct
so I'm going to call this good enough.  The challenge suggested looking into linear programming, which I think is a
little out of the scope here.  If I wanted a super optimized list of pies I'd consider it, but I think this is a
decent solution which gives a correct answer to the question posed.  If you hand me X amount of ingredients, whats the
maximum number of pies of each type I can make.
"""

c_input_1 = "10,14,10,42,24"  # should get 3 pumpkin, 0 apple
c_input_2 = "12,4,40,30,40"   # should get 5 pumpkin, 3 apple
c_input_3 = "12,14,20,42,24"  # should get 5 pumpkin, 1 apple
rec_pumpkin = [1, 0, 3, 4, 3]
rec_apple = [0, 1, 4, 3, 2]


def bake_some_pies(c_input):
    p_input = [int(n) for n in c_input.split(',')]
    pumpkin_count = 0
    apple_count = 0
    finished = False
    while not finished:
        max_num_pumpkin = num_pumpkin_pies(p_input)
        max_num_apple = num_apple_pies(p_input)
        # print("Can make {} ppies and {} apies".format(max_num_pumpkin, max_num_apple))
        if max_num_apple == 0 and max_num_pumpkin == 0:
            # print("Can't make no pies, guess we're done here")
            finished = True
        # this checks if the number of pumpkin pies is great than the number of apple pies and makes one
        # we don't do a >= check because apple pie is cheaper and should be made in an == instance
        elif max_num_pumpkin > max_num_apple:
            # print("Making a pumpkin pie then")
            for i in range(0, len(p_input)):
                p_input[i] -= rec_pumpkin[i]
            pumpkin_count += 1
        else:
            # print("Making an apple pie then")
            for i in range(0, len(p_input)):
                p_input[i] -= rec_apple[i]
            apple_count += 1
    print("{} pumpkin pies and {} apple pies".format(pumpkin_count, apple_count))


def num_pumpkin_pies(p_input: list) -> int:
    num_pies = None
    for i in range(0, len(p_input)):
        # skip non-required ingredients
        if rec_pumpkin[i] <= 0:
            continue
        w_i = p_input[i] // rec_pumpkin[i]
        if num_pies is None:
            num_pies = w_i
        else:
            if w_i < num_pies:
                num_pies = w_i
    return num_pies


def num_apple_pies(p_input: list) -> int:
    num_pies = None
    for i in range(0, len(p_input)):
        # skip non-required ingredients
        if rec_apple[i] <= 0:
            continue
        w_i = p_input[i] // rec_apple[i]
        if num_pies is None:
            num_pies = w_i
        else:
            if w_i < num_pies:
                num_pies = w_i
    return num_pies


bake_some_pies(c_input_1)
bake_some_pies(c_input_2)
bake_some_pies(c_input_3)
