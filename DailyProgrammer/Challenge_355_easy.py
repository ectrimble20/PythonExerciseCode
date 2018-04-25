# Challenge_355_easy.py
"""
Alphabet Cipher

"The Alphabet Cipher", published by Lewis Carroll in 1868, describes a Vigenère cipher (thanks /u/Yadkee for the
clarification) for passing secret messages. The cipher involves alphabet substitution using a shared keyword.
Using the alphabet cipher to transmit messages follows this procedure:

You must make a substitution chart like this, where each row of the alphabet is rotated by one as each letter goes
down the chart. All test cases will utilize this same substitution chart.

Each input will consist of two strings, separate by a space. The first word will be the secret word,
and the second will be the message to encrypt.
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


in_str = str(input("Enter Secret Word And Message to decode: "))
f_idx = in_str.find(" ")  # find first index of space
secret_word = in_str[0:f_idx]
secret_word.strip()
# we don't really care about the secret word, we only really care about the first letter
decode_letter = secret_word[0]
decode_letter.lower()  # make sure it's lowercase so we can find it's index which will be our offset
idx = 0
for i in alphabet:
    if i == decode_letter:
        break
    else:
        idx += 1
message = in_str[f_idx+1:]
message.strip()
print("IDX", idx)

# okay, lets decode the message with our offset
decoded_message = []
for c in message:
    if c == ' ':
        decoded_message.append(" ")
        continue
    c_idx = 0
    for c_i in alphabet:
        if c == c_i:
            f_c_idx = c_idx + idx
            if f_c_idx > 25:
                f_c_idx -= 25  # if we wen't past the 26th char, adjust back down to 0
            print("FC IDX", f_c_idx, "for char", c_i)
            decoded_message.append(alphabet[f_c_idx])
        else:
            c_idx += 1

decoded_message_str = "".join(decoded_message)
print(decoded_message_str)
