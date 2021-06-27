"""
Kata description:

Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if
they consist of four octets, with values between 0 and 255, inclusive.

Input to the function is guaranteed to be a single string.

Examples
Valid inputs:

1.2.3.4
123.45.67.89
Invalid inputs:

1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Note that leading zeros (e.g. 01.02.03.04) are considered invalid.
"""


def is_valid_ip(strng):
    check = strng.split('.')
    if len(check) != 4:
        return False
    for i in check:
        if any(c.isalpha() for c in i) or ' ' in i:
            return False
        if int(i) > 255 or int(i) < 0:
            return False
        if len(i) > 1:
            if int(i[0]) == 0:
                return False
    return True


print(is_valid_ip('1.2.3'))
print(is_valid_ip('123.45.67.89'))
print(is_valid_ip('1.2.3.4'))
print(is_valid_ip('123.456.78.90'))
