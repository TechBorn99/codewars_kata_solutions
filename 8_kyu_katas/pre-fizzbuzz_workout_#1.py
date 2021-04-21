"""
Kata description:

This is the first step to understanding FizzBuzz.

Your inputs: a positive integer, n, greater than or equal to one. n is provided, you have NO CONTROL over its value.

Your expected output is an array of positive integers from 1 to n (inclusive).

Your job is to write an algorithm that gets you from the input to the output.
"""


def pre_fizz(n):
    li = []
    for i in range(1, n + 1):
        li.append(i)
    return li


if __name__ == "__main__":
    print(pre_fizz(1))
    print(pre_fizz(2))
    print(pre_fizz(3))
    print(pre_fizz(4))
    print(pre_fizz(5))
