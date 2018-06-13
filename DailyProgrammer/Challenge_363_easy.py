"""
"I before E except after C" is perhaps the most famous English spelling rule. For the purpose of this challenge,
the rule says:

if "ei" appears in a word, it must immediately follow "c".
If "ie" appears in a word, it must not immediately follow "c".
A word also follows the rule if neither "ei" nor "ie" appears anywhere in the word. Examples of words that follow
this rule are:

fiery hierarchy hieroglyphic
ceiling inconceivable receipt
daily programmer one two three

There are many exceptions that don't follow this rule, such as:

sleigh stein fahrenheit
deifies either nuclei reimburse
ancient juicier societies
"""

words = ["a", "zombie", "transceiver", "veil", "icier"]
# true, true, true, false, false


def check(word):
    if "ei" in word:
        return "cei" in word
    elif "ie" in word:
        return "cie" not in word
    else:
        return True

for w in words:
    print("{} => {}".format(w, check(w)))
