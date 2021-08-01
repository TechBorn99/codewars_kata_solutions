"""
Kata description:

Given a variable n,

If n is an integer, Return a string with dash'-'marks before and after each odd integer, but do not begin or end the
string with a dash mark. If n is negative, then the negative sign should be removed.

If n is not an integer, return an empty value.

Ex:

dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
"""


def dashatize(n):
    list = str(n)
    print(list)
    result = []
    j = k = 0
    if len(list) == 2:
        return list[1]
    for i in list:
        if not i.isnumeric():
            if i == '-':
                continue
            return 'None'
        if int(i) % 2 == 1:
            if k == 0:
                result.append(i)
                result.append('-')
            elif k == len(list) - 1:
                if result[len(result) - 1] != '-':
                    result.append('-')
                result.append(i)
            else:
                if result[len(result) - 1] != '-':
                    result.append('-')
                result.append(i)
                result.append('-')
        else:
            result.append(i)
        k += 1
    return ''.join(result) if result[len(result) - 1] != '-' else ''.join(result[:len(result) - 1])


print(dashatize(274))
print(dashatize(6815))
