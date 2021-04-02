"""
Kata description:

You are provided with an array of positive integers and an additional integer n (n > 1).

Calculate the sum of each value in the array to the nth power. Then subtract the sum of the original array.

Examples
{1, 2, 3}, 3  -->  (1^3 + 2^3 + 3^3 ) - (1 + 2 + 3)  -->  36 - 6  -->  30
{1, 2}, 5     -->  (1^5 + 2^5) - (1 + 2)             -->  33 - 3  -->  30
"""


def modified_sum(a, n):
    sum1 = sum2 = 0
    for num in a:
        sum1 = sum1 + num
        sum2 = sum2 + num ** n

    return sum2 - sum1


if __name__ == '__main__':
    print(modified_sum([1, 2, 3], 3))
    print(modified_sum([1, 2], 5))