"""
Kata description:

Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""


def solution(s):
    words = []
    word = ''
    for i in s:
        if i.isupper():
            words.append(word)
            word = ''
            word += i
        else:
            word += i
    words.append(word)
    return ' '.join(words)


print(solution("camelCasing"))
print(solution("identifier"))
print(solution(""))
