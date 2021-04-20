"""
Kata description:

Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it
should return "Error".
"""


def problem(a):
    if isinstance(a, str):
        return 'Error'
    return a * 50 + 6


if __name__ == "__main__":
    print(problem("hello"))
    print(problem(1))
