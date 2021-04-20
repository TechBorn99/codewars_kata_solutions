"""
Kata description:

Complete the function that calculates the area of the red square, when the length of the circular arc A is given as the
input. Return the result rounded to two decimals.

Graph

Note: use the π value provided in your language (Math::PI, M_PI, math.pi, etc)
"""

import math


def square_area(A):
    r = (2 * A) / math.pi
    return round(r ** 2, 2)


if __name__ == "__main__":
    print(square_area(2))
    print(square_area(0))
    print(square_area(14.05))
    print(square_area(100))
    print(square_area(1))
