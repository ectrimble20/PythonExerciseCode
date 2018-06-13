# ReverseWordOrder.py
"""
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back
to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
"""


def reverse_words(str_of_words):
    t = str_of_words.split(" ")
    t.reverse()
    return " ".join(t)


user_input = input("Type a string with multiple words: ")
# >:( I ain't even fixing this one
print(reverse_words(str(user_input)))

# single liner cuz why not
user_input = " ".join(user_input.split(" ")[::-1])
print(f"{user_input}")
# this walks the string in reverse using list splitting and returns a reversed string
