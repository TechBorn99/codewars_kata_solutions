"""
Kata description:

In this Kata, you will be given an integer array and your task is to return the sum of elements occupying
prime-numbered indices.

The first element of the array is at index 0.

Good luck!
"""


def total(arr):
    suma = 0
    for num in range(0, len(arr)):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                suma += arr[num]
    return suma


if __name__ == "__main__":
    print(total([]))
    print(total([1, 2, 3, 4]))
    print(total([1, 2, 3, 4, 5, 6]))
    print(total([1, 2, 3, 4, 5, 6, 7, 8]))
    print(total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
