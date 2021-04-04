"""
Kata description:

You must implement a function that return the difference between the biggest and the smallest value in a list(lst) received as parameter.

The list(lst) contains integers, that means it may contain some negative numbers.

If the list is empty or contains a single element, return 0.

The list(lst) is not sorted.

max_diff([1, 2, 3, 4]) # return 3, because 4 - 1 == 3
max_diff([1, 2, 3, -4]) # return 7, because 3 - (-4) == 7
Have fun!
"""


def max_diff(lst):
    return 0 if not lst else max(lst) - min(lst)


if __name__ == '__main__':
    print(max_diff([0, 1, 2, 3, 4, 5, 6]))
    print(max_diff([-0, 1, 2, -3, 4, 5, -6]))
    print(max_diff([0, 1, 2, 3, 4, 5, 16]))
    print(max_diff([16]))
    print(max_diff([]))