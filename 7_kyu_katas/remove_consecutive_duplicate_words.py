"""
Kata description:


Your task is to remove all consecutive duplicate words from a string, leaving only first words entries. For example:

"alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"

--> "alpha beta gamma delta alpha beta gamma delta"
"""


def remove_consecutive_duplicates(s):
    new_s = s.split(' ')
    li = [new_s[x - 1] for x in range(1, len(new_s)) if new_s[x] != new_s[x - 1]]
    li.append(new_s[len(new_s) - 1])
    return ' '.join(li)


print(remove_consecutive_duplicates("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))