"""
Kata description:

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number
of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""


def solution(s):
    li = [s[i:i + 2] for i in range(0, len(s), 2)]
    final = []
    for i in li:
        word = ''
        for j in range(len(i)):
            if not i[j].isalnum() or i[j].isnumeric():
                word += '_'
            else:
                word += i[j]
            if len(i) < 2 and j != 1:
                word += '_'
        final.append(word)
    return final


print(solution('abc'))
print(solution('abcdef'))
