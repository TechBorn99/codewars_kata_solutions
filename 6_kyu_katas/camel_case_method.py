"""
Kata description:

Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All
words must have their first letter capitalized without spaces.

For instance:

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
Don't forget to rate this kata! Thanks :)
"""


def camel_case(string):
    result = string.split()
    return ''.join(i.capitalize() for i in result)


print(camel_case('hello case'))
print(camel_case('camel case word'))
