"""
Kata description:

In this Kata, you will be given an array of integers whose elements have both a negative and a positive value, except for one integer that is either only negative or only positive. Your task will be to find that integer.

Examples:

[1, -1, 2, -2, 3] => 3

3 has no matching negative appearance

[-3, 1, 2, 3, -1, -4, -2] => -4

-4 has no matching positive appearance

[1, -1, 2, -2, 3, 3] => 3

(the only-positive or only-negative integer may appear more than once)

Good luck!
"""


def solve(arr):
    nums = []
    for i in arr:
        nums.append(abs(i))
    for i in arr:
        if nums.count(abs(i)) == 1 or i - 2 * i not in arr:
            return i


if __name__ == "__main__":
    print(solve([1, -1, 2, -2, 3]))
    print(solve([-3, 1, 2, 3, -1, -4, -2]))
    print(solve([1, -1, 2, -2, 3, 3]))
    print(solve([-110, 110, -38, -38, -62, 62, -38, -38, -38]))
    print(solve([-9, -105, -9, -9, -9, -9, 105]))