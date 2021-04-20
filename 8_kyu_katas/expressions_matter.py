"""
Kata description:

Task
Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and
brackets: +, *, ()
In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained
Consider an Example :
With the numbers are 1, 2 and 3 , here are some ways of placing signs and brackets:

1 * (2 + 3) = 5
1 * 2 * 3 = 6
1 + 2 * 3 = 7
(1 + 2) * 3 = 9
So the maximum value that you can obtain is 9.

Notes
The numbers are always positive.
The numbers are in the range (1  ≤  a, b, c  ≤  10).
You can use the same operation more than once.
It's not necessary to place all the signs and brackets.
Repetition in numbers may occur .
You cannot swap the operands. For instance, in the given example you cannot get expression (1 + 3) * 2 = 8.
Input >> Output Examples:
expressionsMatter(1,2,3)  ==>  return 9
Explanation:
After placing signs and brackets, the Maximum value obtained from the expression (1+2) * 3 = 9.

expressionsMatter(1,1,1)  ==>  return 3
Explanation:
After placing signs, the Maximum value obtained from the expression is 1 + 1 + 1 = 3.
"""


def expression_matter(a, b, c):
    maxi = a * (b + c)

    if a * b * c > maxi:
        maxi = a * b * c
    if a + b * c > maxi:
        maxi = a + b * c
    if (a + b) * c > maxi:
        maxi = (a + b) * c
    if a + b + c > maxi:
        maxi = a + b + c

    return maxi


if __name__ == "__main__":
    print(expression_matter(2, 1, 2))
    print(expression_matter(2, 1, 1))
    print(expression_matter(2, 2, 4))
    print(expression_matter(3, 3, 3))

