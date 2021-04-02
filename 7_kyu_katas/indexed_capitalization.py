"""
Kata description:
Given a string and an array of integers representing indices, capitalize all letters at the given indices.

For example:

capitalize("abcdef",[1,2,5]) = "aBCdeF"
capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.
The input will be a lowercase string with no spaces and an array of digits.

Good luck!
"""


def capitalize(s, ind):
    new_string = ''
    for i in range(len(s)):
        if i in ind:
            new_string += s[i].upper()
        else:
            new_string += s[i]

    return new_string


if __name__ == "__main__":
    print(capitalize("abcdef", [1, 2, 5]))
    print(capitalize("abcdef", [1, 2, 5, 100]))
