"""
Kat adescription:

Your job is to change the given string s using a non-negative integer n.

Each bit in n will specify whether or not to swap the case for each alphabetic character in s: if the bit is 1, swap
the case; if its 0, leave it as is. When you finished with the last bit of n, start again with the first bit.

You should skip the checking of bits when a non-alphabetic character is encountered, but they should be preserved in
their original positions.

Examples
swap('Hello world!', 11)  -->  'heLLO wORLd!'
...because 11 is 1011 in binary, so the 1st, 3rd, 4th, 5th, 7th, 8th and 9th alphabetical characters have to be swapped:

H e l l o  w o r l d !
1 0 1 1 1  0 1 1 1 0
^   ^ ^ ^    ^ ^ ^
More examples:

swap("gOOd MOrniNg", 7864)  -->  "GooD MorNIng"
swap('', 11345)  -->  ''
swap('the lord of the rings', 0)  -->  'the lord of the rings'
"""


def swap(s, n):
    temp = '{0:0b}'.format(n)
    while len(temp) < len(s):
        temp += temp * 2
    new_s = ''
    i2 = 0
    for i in range(len(s)):
        if temp[i2] == '1' and s[i] != ' ' and s[i].isalnum():
            if s[i].isupper():
                new_s += s[i].lower()
            else:
                new_s += s[i].upper()
            i2 += 1
        elif s[i] == ' ' or not s[i].isalnum():
            new_s += s[i]
        else:
            new_s += s[i]
            i2 += 1
    return new_s


if __name__ == "__main__":
    print(swap('Hello world!', 11))
    print(swap("gOOd MOrniNg", 7864))
    print(swap('', 11345))
    print(swap('the lord of the rings', 0))