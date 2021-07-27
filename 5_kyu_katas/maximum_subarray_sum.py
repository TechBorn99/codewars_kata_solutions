"""
Kata description:

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of
integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If
the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
"""


def max_sequence(arr):
    sums = []
    for j, e in enumerate(arr):
        sums.append(e)
        for i in range(j + 1, len(arr)):
            e += arr[i]
            sums.append(e)
    if all(i < 0 for i in arr) or not sums:
        return 0
    else:
        max_sum = max(sums)
        return max_sum


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
