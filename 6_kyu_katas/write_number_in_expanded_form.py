"""
Kata description:

Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
"""


def expanded_form(num):
    temp = []
    while num != 0:
        temp.append(num % 10)
        num = num // 10
    new_temp = []
    counter = 0
    for i in temp:
        new_temp.append(str(i) + '0' * counter)
        counter += 1
    new_temp.reverse()
    return ' + '.join(x for x in new_temp if x.count('0') is not len(x))


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))
