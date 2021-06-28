"""
Kata description:

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result
should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""


def count(string):
    result = {}
    if string == '':
        return {}
    for i in set(string):
        result[i] = string.count(i)
    return result


print(count('aba'))
