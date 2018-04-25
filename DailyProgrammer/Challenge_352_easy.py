# Challenge_352_easy.py
"""
Short links have been all the rage for several years now, spurred in part by Twitter's character limits.
Imgur - Reddit's go-to image hosting site - uses a similar style for their links. Monotonically increasing
IDs represented in Base62.

Your task today is to convert a number to its Base62 representation.

You'll be given one number per line. Assume this is your alphabet:

0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

Example input:

15674
7026425611433322325

Your program should emit the number represented in Base62 notation.

Examples:

O44
bDcRfbr63n8


TBH, I didn't really get wtf they were talking about with the base62, I had to look up what it was referring
to and look at others code to get an idea of what it's doing.

Basically, it's taking w/e number you enter in and dividing it by 62 and using the remainder of the results
which can be grabbed with divmod as the second return using tuple unpacking as the key for the letter since
it will always be 0->62.

So for a visual example, take the first example input: 15674
We divide that by 62 and get the remainder, so basically
15674 % 62 = remainder
15674 // 62 = new number

So after we divide, which divmod is the function that returns both answers we need
the number is redefined as the return of N/62, so in our case we get:
15674 // 62 = 252
15674 % 62 = 50

So we set the first encoded character to the 50th element in our alphabet array, which is "O" (thats the letter)

Now we do the same thing to 252
252 % 62 = 4
252 // 62 = 4

The forth index in now 4 (alphabet is zero indexed as usual btw)
Our encoded string is now "O4"

So now we say
4 % 62
4 // 62

But because it's not divisible it returns itself, so we get 4 again which is 4 in our alphabet
so our encoded string is now "O44"
"""

alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode(num):
    encoded = []
    while num:
        num, remainder = divmod(num, 62)
        encoded.append(alphabet[remainder])
    return ''.join(encoded)


print("{} -> {} : expect {}".format(15674, encode(15674), "O44"))
print("{} -> {} : expect {}".format(7026425611433322325, encode(7026425611433322325), "bDcRfbr63n8"))


"""
from string import digits, ascii_letters

_ALPHABET = digits + ascii_letters

base62 = lambda n: (n == 0 and _ALPHABET[0]) or (_ALPHABET[n % 62] + base62(n // 62).lstrip(_ALPHABET[0]))

def encode(num, alphabet):
    result = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        result.append(alphabet[rem])
    return ''.join(result)

if __name__ == "__main__":
    import string
    alphabet = string.digits + string.ascii_letters
    print(encode(18752, alphabet)) # sS4
"""