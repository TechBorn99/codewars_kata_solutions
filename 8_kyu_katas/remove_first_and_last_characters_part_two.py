"""
Kata description:

This is a spin off of my first kata. You are given a list of character sequences as a comma separated string. Write a
function which returns another string containing all the character sequences except the first and the last ones,
separated by spaces. If the input string is empty, or the removal of the first and last items would cause the string
to be empty, return a null value.
"""


def array(string):
    s = string.split(',')
    s2 = ' '.join(s[1:len(s) - 1])
    return s2 if s2 != '' else None


if __name__ == "__main__":
    print(array(''))
    print(array('1'))
    print(array('1, 3'))
    print(array('1,2,3'))
    print(array('1,2,3,4'))
