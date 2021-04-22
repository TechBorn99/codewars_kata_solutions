"""
Kata description:

Write a function that checks if all the letters in the second string are present in the first one at least once,
regardless of how many times they appear:

["ab", "aaa"]    =>  true
["trances", "nectar"]    =>  true
["compadres", "DRAPES"]  =>  true
["parses", "parsecs"]    =>  false
Function should not be case sensitive, as indicated in example #2. Note: both strings are presented as a single
argument in the form of an array.
"""


def letter_check(arr):
    for i in arr[1].lower():
        if i not in arr[0].lower():
            return False
    return True


if __name__ == "__main__":
    print(letter_check(["ab", "aaa"]))
    print(letter_check(["trances", "nectar"]))
    print(letter_check(["compadres", "DRAPES"]))
    print(letter_check(["parses", "parsecs"]))

