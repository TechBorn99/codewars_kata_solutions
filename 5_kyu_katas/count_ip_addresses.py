"""
Kata description:

Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the
first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first
one.

Examples
ips_between("10.0.0.0", "10.0.0.50")  ==   50
ips_between("10.0.0.0", "10.0.1.0")   ==  256
ips_between("20.0.0.10", "20.0.1.0")  ==  246
"""


def ips_between(start, end):
    li = start.split('.')
    li2 = end.split('.')

    first = (int(li2[0]) - int(li[0])) * 256 * 256 * 256
    second = (int(li2[1]) - int(li[1])) * 256 * 256
    third = (int(li2[2]) - int(li[2])) * 256
    fourth = int(li2[3]) - int(li[3])

    return sum([first, second, third, fourth])


print(ips_between("10.0.0.0", "10.0.0.50"))
print(ips_between("10.0.0.0", "10.0.1.0"))
print(ips_between("20.0.0.10", "20.0.1.0"))
