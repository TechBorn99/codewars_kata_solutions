"""
Kata description:

The following was a question that I received during a technical interview for an entry level software developer
 position. I thought I'd post it here so that everyone could give it a go:

You are given an unsorted array containing all the integers from 0 to 100 inclusively. However, one number is missing.
Write a function to find and return this number. What are the time and space complexities of your solution?
"""


def missing_no(nums):
    nums.sort()
    list = range(0, 101)

    for i in list:
        if i == 100:
            return i
        if nums[i] != list[i]:
            return list[i]


if __name__ == '__main__':

    l1 = list(range(0, 101))
    l2 = list(range(0, 101))
    l1.remove(5)
    l2.remove(10)
    print(missing_no(l1))
    print(missing_no(l2))