# Challenge_353_easy.py
"""
In theoretical computer science, the closest string is an NP-hard computational problem, which tries to find the
geometrical center of a set of input strings. To understand the word "center", it is necessary to define a distance
between two strings. Usually, this problem is studied with the Hamming distance in mind. This center must be one of
the input strings.

In bioinformatics, the closest string problem is an intensively studied facet of the problem of finding signals in DNA.
In keeping with the bioinformatics utility, we'll use DNA sequences as examples.

Consider the following DNA sequences:

ATCAATATCAA
ATTAAATAACT
AATCCTTAAAC
CTACTTTCTTT
TCCCATCCTTT
ACTTCAATATA

Using the Hamming distance (the number of different characters between two sequences of the same length), the all-pairs
distances of the above 6 sequences puts ATTAAATAACT at the center.


This was pretty easy, I didn't really "optimize" or pythanize or w/e people call it.

Really only needed to figure out which line has the most common characters with the other lines.
To do this, I took each line, compared it with every other line and for each character that matched
I incremented it's "score".  Then compared it's score to the existing score and if it's higher, that
line is now assigned as the closest to center.

Then it's just a matter of looping on the strings and returning the one with the most matches.
"""


def find_closest_string(lines: list):
    closest_line = ""
    closest_line_total = 0
    for line in lines:
        line_total = 0
        for s in lines:
            if line != s:
                for i, c in enumerate(s):
                    if c == line[i]:
                        line_total += 1
        if line_total > closest_line_total:
            closest_line = line
            closest_line_total = line_total
    return closest_line

test = [
    "ATCAATATCAA",
    "ATTAAATAACT",
    "AATCCTTAAAC",
    "CTACTTTCTTT",
    "TCCCATCCTTT",
    "ACTTCAATATA",
]

print("Closest: {}".format(find_closest_string(test)))

challenge_1 = [
    "AACACCCTATA",
    "CTTCATCCACA",
    "TTTCAATTTTC",
    "ACAATCAAACC",
    "ATTCTACAACT",
    "ATTCCTTATTC",
    "ACTTCTCTATT",
    "TAAAACTCACC",
    "CTTTTCCCACC",
    "ACCTTTTCTCA",
    "TACCACTACTT"
]

challenge_2 = [
    "ACAAAATCCTATCAAAAACTACCATACCAAT",
    "ACTATACTTCTAATATCATTCATTACACTTT",
    "TTAACTCCCATTATATATTATTAATTTACCC",
    "CCAACATACTAAACTTATTTTTTAACTACCA",
    "TTCTAAACATTACTCCTACACCTACATACCT",
    "ATCATCAATTACCTAATAATTCCCAATTTAT",
    "TCCCTAATCATACCATTTTACACTCAAAAAC",
    "AATTCAAACTTTACACACCCCTCTCATCATC",
    "CTCCATCTTATCATATAATAAACCAAATTTA",
    "AAAAATCCATCATTTTTTAATTCCATTCCTT",
    "CCACTCCAAACACAAAATTATTACAATAACA",
    "ATATTTACTCACACAAACAATTACCATCACA",
    "TTCAAATACAAATCTCAAAATCACCTTATTT",
    "TCCTTTAACAACTTCCCTTATCTATCTATTC",
    "CATCCATCCCAAAACTCTCACACATAACAAC",
    "ATTACTTATACAAAATAACTACTCCCCAATA",
    "TATATTTTAACCACTTACCAAAATCTCTACT",
    "TCTTTTATATCCATAAATCCAACAACTCCTA",
    "CTCTCAAACATATATTTCTATAACTCTTATC",
    "ACAAATAATAAAACATCCATTTCATTCATAA",
    "CACCACCAAACCTTATAATCCCCAACCACAC"
]

print("Challenge 1: {}".format(find_closest_string(challenge_1)))
# expect ATTCTACAACT
print("Challenge 2: {}".format(find_closest_string(challenge_2)))
# expect TTAACTCCCATTATATATTATTAATTTACCC
