"""
Kata description:

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
Return the resulting string.
"""


def fake_bin(x):
    return ''.join(map(str, ['0' if i < '5' else '1' for i in x]))


if __name__ == "__main__":
    print(fake_bin("45385593107843568"))
    print(fake_bin("509321967506747"))
    print(fake_bin("366058562030849490134388085"))
    print(fake_bin("15889923"))
    print(fake_bin("800857237867"))