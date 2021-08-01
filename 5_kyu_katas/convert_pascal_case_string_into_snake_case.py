"""
Kata description:

Complete the function/method so that it takes CamelCase string and returns the string in snake_case notation.
Lowercase characters can be numbers. If method gets number, it should return string.

Examples:

# returns test_controller
to_underscore('TestController')

# returns movies_and_books
to_underscore('MoviesAndBooks')

# returns app7_test
to_underscore('App7Test')

# returns "1"
to_underscore(1)
"""

import re


def to_underscore(string):
    return str(string) if type(string) == int else '_'.join(x.lower() for x in re.findall('[A-Z][^A-Z]*', string))


print(to_underscore('TestController'))
print(to_underscore('MoviesAndBooks'))
print(to_underscore(1))
