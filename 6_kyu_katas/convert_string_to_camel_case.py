"""
Kata description:

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word
within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also
often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""


def to_camel_case(text):
    i = 0
    result = ''
    while i < len(text):
        if i >= len(text):
            break
        if text[i] == '-' or text[i] == '_':
            result += text[i + 1].upper()
            i += 1
        else:
            result += text[i]
        i += 1
    return result


print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))
