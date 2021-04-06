"""
Kata description:

In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to
convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
For example:

solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowercase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
More examples in test cases. Good luck!
"""


def solve(s):
    upp = down = 0
    for i in s:
        if i.isupper():
            upp += 1
        else:
            down += 1
    return s.upper() if upp > down else s.lower()


if __name__ == "__main__":
    print(solve("coDe"))
    print(solve("CODe"))
    print(solve("coDE"))