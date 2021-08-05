"""
Kata description:

Description:

We want to generate a function that computes the series starting from 0 and ending until the given number.

Example:
Input:

> 6
Output:

0+1+2+3+4+5+6 = 21

Input:

> -15
Output:

-15<0

Input:

> 0
Output:

0=0
"""


def show_sequence(n):
    if n > 0:
        result = [i for i in range(n + 1)]
        result = '+'.join(str(result[i]) for i in result)
        return result + ' = {}'.format(str(sum(i for i in range(n + 1))))
    elif n == 0:
        return '0=0'.format(n)
    else:
        return '{}<0'.format(n)


print(show_sequence(6))
print(show_sequence(-15))
print(show_sequence(0))
