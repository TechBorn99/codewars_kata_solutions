"""
Kata description:

Complete the solution. It should try to retrieve the value of the array at the index provided. If the index is out of
the array's max bounds then it should return the default value instead.

Example:

data = ['a', 'b', 'c']
solution(data, 1, 'd') # should == 'b'
solution(data, 5, 'd') # should == 'd'

# negative values work as long as they aren't out of the length bounds
solution(data, -1, 'd') # should == 'c'
solution(data, -5, 'd') # should == 'd'
"""


def solution(items, index, default_value):
    counter = 0
    if index >= 0:
        for i in items:
            if counter == index:
                return i
            counter += 1
    else:
        for i in items[::-1]:
            counter += 1
            if counter == abs(index):
                return i

    return default_value


if __name__ == "__main__":
    print(solution(['a', 'b', 'c'], 1, 'd'))
    print(solution(['a', 'b', 'c'], 5, 'd'))
    print(solution(['a', 'b', 'c'], -1, 'd'))
