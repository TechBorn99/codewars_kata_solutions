"""
Kata description:

Acknowledgments:
I thank yvonne-liu for the idea and for the example tests :)

Description:
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter needs to be converted to its ASCII code.
The second letter needs to be switched with the last letter
Keepin' it simple: There are no special characters in input.
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
"""


def encrypt_this(text):
    if not text:
        return ''
    temp = text.split(' ')
    result = []
    for i in temp:
        word = ''
        word += str(ord(i[0]))
        tmp = list(i[1:])
        if len(i) > 2:
            tmp[0], tmp[len(tmp) - 1] = tmp[len(tmp) - 1], tmp[0]
        word += ''.join(tmp)
        result.append(word)
    return ' '.join(result)


print(encrypt_this("Hello"))
print(encrypt_this("good"))
print(encrypt_this("hello world"))
