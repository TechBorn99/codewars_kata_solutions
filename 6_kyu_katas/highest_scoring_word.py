"""
Kata description:

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""


def high(x):
    words = x.split()
    maxi = sum([(ord(x) - 96) for x in words[0]])
    result = words[0]
    for word in words:
        new_max = 0
        for letter in word:
            new_max += ord(letter) - 96
        if new_max > maxi:
            result = word
            maxi = new_max
    return result


print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))
