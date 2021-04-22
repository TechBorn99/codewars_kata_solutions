"""
Kata description:

Make a function "add" that will be able to sum elements of list continuously and return a new list of sums.

For example:

add [1,2,3,4,5] == [1, 3, 6, 10, 15], because it's calculated like
this : [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4, 1 + 2 + 3 + 4 + 5]
"""


def add(l):
    new_list = []
    for i in range(len(l)):
        index = 0
        j = l[index]
        while index != i:
            index += 1
            j += l[index]
        new_list.append(j)

    return new_list


if __name__ == "__main__":
    print(add([1, 2, 3, 4, 5]))
