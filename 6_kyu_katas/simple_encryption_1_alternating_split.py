"""
Kata description:

For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
Write two methods:

def encrypt(text, n)
def decrypt(encrypted_text, n)
For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.
"""


def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text
    while n != 0:
        first = encrypted_text[:len(encrypted_text) // 2]
        second = encrypted_text[len(encrypted_text) // 2:]
        new_text = ''
        j = k = 0
        for i in range(len(encrypted_text)):
            if i % 2 == 0:
                new_text += second[j]
                j += 1
            else:
                new_text += first[k]
                k += 1
        encrypted_text = new_text
        n -= 1
    return encrypted_text


def encrypt(text, n):
    if not text or n <= 0:
        return text
    while n != 0:
        first = ''
        for i in range(len(text)):
            if i % 2 == 1:
                first += text[i]
        text = first + text[::2]
        n -= 1
    return text


print(encrypt("This is a test!", 2))
print(encrypt("This is a test!", 1))
