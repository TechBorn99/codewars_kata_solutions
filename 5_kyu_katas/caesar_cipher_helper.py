"""
Kata description:

Write a class that, when given a string, will return an uppercase string with each letter shifted forward in the
alphabet by however many spots the cipher was initialized to.

For example:

c = CaesarCipher(5); # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
c.decode('BFKKQJX') # returns 'WAFFLES'
If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
The shift will always be in range of [1, 26].
"""

import string


class CaesarCipher(object):
    shift = None
    alphabet = string.ascii_lowercase

    def __init__(self, shift):
        self.shift = shift

    def encode(self, st):
        result = ''
        for i in st:
            if i.isalpha():
                result += self.alphabet[(self.alphabet.index(i.lower()) + self.shift) % 26].upper()
            else:
                result += i
        return result

    def decode(self, st):
        result = ''
        for i in st:
            if i.isalpha():
                result += self.alphabet[(self.alphabet.upper().index(i) - self.shift)].upper()
            else:
                result += i
        return result


if __name__ == "__main__":
    c = CaesarCipher(5)
    print(c.encode('Codewars'))
    print(c.decode('HTIJBFWX'))
