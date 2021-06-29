"""
Kata description:

Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match
str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""


def scramble(s1, s2):
    return [False if s1.count(i) < s2.count(i) else True for i in set(s2)].count(False) == 0


print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
