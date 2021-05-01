"""
Kata description:

Is the number even?
If the numbers is even return true. If it's odd, return false.


Oh yeah... the following symbols/commands have been disabled!

use of ```%```
use of ```.even?``` in Ruby
use of ```mod``` in Python
"""


def is_even(n):
    return n ^ 1 == n + 1


if __name__ == "__main__":
    print(is_even(1))
    print(is_even(2))
    print(is_even(3))
    print(is_even(10))
