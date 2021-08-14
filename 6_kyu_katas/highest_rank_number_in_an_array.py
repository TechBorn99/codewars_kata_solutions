"""
Kata description:

Complete the method which returns the number which is most frequent in the given input array. If there is a tie for
most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
"""


def highest_rank(arr):
    element = arr[0]
    for i in set(arr):
        if arr.count(element) < arr.count(i):
            element = i
        elif arr.count(element) == arr.count(i):
            element = max(element, i)
    return element


print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]))
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]))
print(highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]))
