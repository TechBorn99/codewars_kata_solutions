"""
Kata description:

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the
alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet
should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""

import string


def rot13(message):
    lower = dict(zip(range(97, 123), string.ascii_lowercase))
    upper = dict(zip(range(65, 91), string.ascii_uppercase))
    result = ''
    for i in message:
        num = 13
        if i.isalpha():
            if i.islower():
                if (ord(i) + num) <= 122:
                    result += lower[ord(i) + num]
                else:
                    if (ord(i) - num) >= 97:
                        result += lower[ord(i) - num]
                    else:
                        num = 97 - (97 - 13)
                        result += upper[90 - num]
            else:
                if (ord(i) + num) <= 90:
                    result += upper[ord(i) + num]
                else:
                    if (ord(i) - num) >= 65:
                        result += upper[ord(i) - num]
                    else:
                        num = 65 - (65 - 13)
                        result += lower[122 - num]
        else:
            result += i
    return result


print(rot13("test"))
print(rot13("Test"))
