"""
Kata description:

A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The
range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at
least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string
in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
Courtesy of rosettacode.org
"""


def solution(args):
    result = ''
    check = [-1, 1]
    i = 0
    while i < len(args[:len(args) - 1]):
        temp = []
        curr = args[i]
        next = args[i + 1]
        if next - curr in check:
            temp.append(curr)
            while next - curr in check:
                temp.append(next)
                i += 1
                if i >= len(args[:len(args) - 1]):
                    break
                curr = args[i]
                next = args[i + 1]
            if len(temp) > 2:
                result += '?'.join([str(min(temp)), str(max(temp))]) + ','
            else:
                result += '{},{},'.format(temp[0], temp[1])
        else:
            temp.append(curr)
            result += '{},'.format(temp[0])
        i += 1
    last_check = result[:len(result) - 1].split(',')[-1].split('?')
    last_check.reverse()
    if last_check[0] == str(args[-1]):
        result = result.replace('?', '-')
        return result[:len(result) - 1]
    else:
        result = result.replace('?', '-')
        return result[:len(result) - 1] + ',{}'.format(args[-1])


print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
