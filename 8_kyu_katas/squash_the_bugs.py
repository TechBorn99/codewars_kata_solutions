"""
Kata description:

Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value.
Output should be the length of the longest word, as a number.

There will only be one 'longest' word.
"""


def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i = 0
    while i < len(spl):
        if len(spl[i]) > longest:
            longest = len(spl[i])
        i += 1
    return longest


if __name__ == "__main__":
    print(find_longest("The quick white fox jumped around the massive dog"))
    print(find_longest("Take me to tinseltown with you"))
    print(find_longest("Sausage chops"))
    print(find_longest("Wind your body and wiggle your belly"))
