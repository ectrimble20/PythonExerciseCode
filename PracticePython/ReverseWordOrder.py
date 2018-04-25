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
print(reverse_words(str(user_input)))
