"""
Kata description:

Task
Given a positive integer n, calculate the following sum:

n + n/2 + n/4 + n/8 + ...
All elements of the sum are the results of integer division.

Example
25  =>  25 + 12 + 6 + 3 + 1 = 47
"""


def halving_sum(n):
    sm = 0
    while n >= 1:
        sm += n
        n = int(n / 2)
    return sm


if __name__ == '__main__':
    print(halving_sum(25))
    print(halving_sum(127))