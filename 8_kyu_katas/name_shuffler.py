"""
Kata description:

Write a function that returns a string in which firstname is swapped with last name.

name_shuffler('john McClane'); => "McClane john"
"""


def name_shuffler(str_):
    list = str_.split(' ')
    list.reverse()
    return ' '.join(list)


if __name__ == "__main__":
    print(name_shuffler("john McClane"))
