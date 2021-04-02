"""
Kata description:

Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!
"""


def capitalize(s):
    new_s = ""
    for i in range(len(s)):
        if i % 2 == 0:
            new_s = new_s + s[i].upper()
        else:
            new_s = new_s + s[i].lower()

    new_s2 = ""

    for i in range(len(s)):
        if i % 2 == 1:
            new_s2 = new_s2 + s[i].upper()
        else:
            new_s2 = new_s2 + s[i].lower()

    return [new_s, new_s2]


if __name__ == '__main__':

    print(capitalize('abcdef'))
    print(capitalize('codewarriors'))
