"""
Kata description:

In mathematics, Pascal's triangle is a triangular array of the binomial coefficients expressed with formula

(nk)=n!k!(n−k)!\lparen {n \atop k} \rparen = \frac {n!} {k!(n-k)!}(
k
n
​
 )=
k!(n−k)!
n!
​

where n denotes a row of the triangle, and k is a position of a term in the row.

Pascal's Triangle

You can read Wikipedia article on Pascal's Triangle for more information.

Task
Write a function that, given a depth n, returns n top rows of Pascal's Triangle flattened into a one-dimensional
list/array.

Example:
n = 1: [1]
n = 2: [1,  1, 1]
n = 4: [1,  1, 1,  1, 2, 1,  1, 3, 3, 1]
"""

import functools
import operator


def pascals_triangle(n):
    answer = [[1]]
    for size in range(2, n + 1):
        tmp = [1] * size
        for i in range(1, size - 1):
            tmp[i] = answer[-1][i] + answer[-1][i - 1]
        answer.append(tmp)
    return functools.reduce(operator.iconcat, answer, [])


print(pascals_triangle(1))
print(pascals_triangle(2))
print(pascals_triangle(4))
