# Challenge_358_easy.py
"""
For this challenge, you will receive 3 lines of input, with each line being 27 characters long (representing 9 total
numbers), with the digits spread across the 3 lines. Your job is to return the represented digits. You don't need to
account for odd spacing or missing segments.

Output Description
"""

# list of deciphered inputs
cheat_sheet = {
    '     |  |': "1",
    ' _  _||_ ': "2",
    ' _  _| _|': "3",
    '   |_|  |': "4",
    ' _ |_  _|': "5",
    ' _ |_ |_|': "6",
    ' _   |  |': "7",
    ' _ |_||_|': "8",
    ' _ |_| _|': "9",
    ' _ | ||_|': "0"
}


def decipher(line: str):
    rows = line.split("\n")
    # we know we're getting 27 chars, we need to read 3 chars per character per row to form an actual character code
    characters = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
    for i in range(9):
        for j in range(3):
            r = rows[j]
            characters[i+1] += r[i*3:(i*3)+3]
    ciphered = []
    for k, v in characters.items():
        ciphered.append(cheat_sheet.get(v, "[ERR ON {}]".format(k)))
    return "".join(ciphered)

# to make it interactive, change line = "" to line = input() + input() + input()
# Note:  This is crazy susceptible to breaking if spaces are out of place, this isn't really
# a good exercise (IMO of course) as it doesn't require error checking or enforcement of any
# of the rules of the exercise.
line_test1 = """ _  _        _  _  _  _  _
|_||_ |_|  || ||_ |_ |_| _|
 _| _|  |  ||_| _| _| _||_ """
# should return 954105592

# NOTE: this break cuz my IDE doesn't like white-space at the end of a string
line_test2 = """    _  _     _  _  _  _  _
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|"""
# should return 123456789

print(decipher(line_test1))
print(decipher(line_test2))
