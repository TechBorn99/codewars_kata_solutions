"""
Kata description:

Your task is to sort a given string. Each word in the string will contain a single number. This number is the position
the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive
numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""

import re


def order(sentence):
    lst = sentence.split()
    temp = re.findall(r'\d+', sentence)
    pos = list(map(int, temp))

    for i in range(len(pos)):
        for j in range(0, len(pos) - i - 1):
            if pos[j] > pos[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                pos[j], pos[j + 1] = pos[j + 1], pos[j]

    result = ' '.join(lst)

    return result


if __name__ == "__main__":
    print(order("is2 Thi1s T4est 3a"))
    print(order("4of Fo1r pe6ople g3ood th5e the2"))
