"""
Kata description:

Impliment the reverse function, which takes in input n and reverses it. For instance, reverse(123) should return 321.
You should do this without converting the inputted number into a string.

# Please do not use anything from the following list:
['encode','decode','join','zfill','codecs','chr','bytes','ascii', 'substitute','template','bin', 'os','sys','re', '"',
"'", 'str','repr', '%s', 'format', 'type', '__', '.keys','eval','exec','subprocess']
"""


def reverse(n):
    new_n = 0
    while n is not 0:
        r = int(n % 10)
        new_n = new_n * 10 + r
        n = n // 10
    return new_n


print(reverse(1234))
print(reverse(10987))
print(reverse(1020))
