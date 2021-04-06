"""
Kata description:

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array
is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""


def find_outlier(integers):
    outlier = integers[0]

    if (integers[0] % 2 == 0 and integers[1] % 2 == 0) or (
            integers[len(integers) - 1] % 2 == 0 and integers[len(integers) - 2] % 2 == 0) or (
            integers[len(integers) - 1] % 2 == 0 and integers[len(integers) - 2] % 2 == 0) or (
            integers[len(integers) - 1] % 2 == 0 and integers[0] % 2 == 0):
        for i in integers:
            if i % 2 == 1:
                outlier = i
    else:
        for i in integers:
            if i % 2 == 0:
                outlier = i

    return outlier


if __name__ == "__main__":
    print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
    print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))

