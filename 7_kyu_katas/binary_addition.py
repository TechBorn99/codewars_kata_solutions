"""
Kata description:

Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before,
or after the addition.

The binary number returned should be a string.

Examples:

add_binary(1, 1) == "10" (1 + 1 = 2 in decimal or 10 in binary)
add_binary(5, 9) == "1110" (5 + 9 = 14 in decimal or 1110 in binary)
"""


def add_binary(a, b):
    binary = [int(i) for i in list('{0:0b}'.format(a + b))]
    return ''.join([str(x) for x in binary])


print(add_binary(1, 1))
print(add_binary(5, 9))
