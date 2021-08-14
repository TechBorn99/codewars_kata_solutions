"""
Kata description:

Modify the kebabize function so that it converts a camel case string into a kebab case.

kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps
Notes:

the returned string should only contain lowercase letters
"""


def kebabize(string):
    result = ''
    if string[0].isupper():
        result += string[0].lower()
    for i in range(len(string) - 1):
        if string[i].islower():
            result += string[i]
        if string[i + 1].isupper():
            result += '-{}'.format(string[i + 1].lower())
    if string[-1].islower():
        result += string[-1]
    if result != '':
        return result if result[0] != '-' else result[1:]
    else:
        return ''


print(kebabize('camelsHaveThreeHumps'))
print(kebabize('camelsHave3Humps'))
