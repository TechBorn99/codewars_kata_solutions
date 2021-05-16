"""
Kata description:

Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string
should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""


def reverse_words(text):
    words = text.split(' ')
    result = []
    for i in words:
        result.append(i[::-1])
    return ' '.join(result)


print(reverse_words("This is an example!"))
print(reverse_words("double  spaces"))
