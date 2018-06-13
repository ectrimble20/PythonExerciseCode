# PasswordGenerator.py
import random
"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords
have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random,
generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""

# allowed characters
alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
               'x', 'y', 'z']
alpha_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
               'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['@', '#', '$', '%', '&']

# FYI, just use a string, you can iterate a string exactly like a list.

strong = {'alpha_l': 3, 'alpha_u': 2, 'numbers': 3, 'special': 2, 'length': 10}
medium = {'alpha_l': 3, 'alpha_u': 2, 'numbers': 2, 'special': 1, 'length': 8}
weak = {'alpha_l': 3, 'alpha_u': 2, 'numbers': 1, 'special': 0, 'length': 6}


def get_user_choice():
    while True:
        user_selection = int(input("Please select your password strength (1) Strong (2) Medium (3) Weak:"))
        # user_selection = int(user_selection)  # damnit man
        if user_selection not in [1, 2, 3]:
            print("Please enter a valid choice (1, 2 or 3)")
            continue
        return user_selection


def gen_password(strength):
    gen_list = {}  # this is just cuz my IDE is complaining
    if strength == 1:
        gen_list = strong
    if strength == 2:
        gen_list = medium
    if strength == 3:
        gen_list = weak
    pw_as_list = []
    for _ in range(0, gen_list['alpha_l']):
        rand_index = random.randint(0, len(alpha_lower)-1)
        pw_as_list.append(alpha_lower[rand_index])
    for _ in range(0, gen_list['alpha_u']):
        rand_index = random.randint(0, len(alpha_upper) - 1)
        pw_as_list.append(alpha_upper[rand_index])
    for _ in range(0, gen_list['numbers']):
        rand_index = random.randint(0, len(numbers)-1)
        pw_as_list.append(numbers[rand_index])
    for _ in range(0, gen_list['special']):
        rand_index = random.randint(0, len(special)-1)
        pw_as_list.append(special[rand_index])
    pw_as_list.reverse()  # FYI reverse is an in-place operation ;)
    random.shuffle(pw_as_list)  # FYI shuffle is also an in-place operation
    return "".join(pw_as_list)


# Test, lets see what this, or even if this generates something
print("Strong:", gen_password(1))
print("Medium:", gen_password(2))
print("Weak:", gen_password(3))

#if __name__ == '__main__':
#    print(gen_password(get_user_choice()))
