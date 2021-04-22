"""
Kata description:

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""


def get_count(input_str):
    num_vowels = 0
    for i in input_str:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            num_vowels += 1
    return num_vowels


if __name__ == "__main__":
    print(get_count("abracadabra"))
    print(get_count("pear tree"))
    print(get_count(""))
