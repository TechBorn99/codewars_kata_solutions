"""
Kata description:

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the
other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(array):
    if len(array) == 1:
        return array
    num_of_zeros = array.count(0)
    i = 0
    while num_of_zeros is not 0:
        if array[i] == 0 and array[i] is not False:
            array.append(array.pop(i))
            i -= 1
            num_of_zeros -= 1
        i += 1
    return array