"""
Kata description:

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks
untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text):
    result = []
    for i in text.split():
        if i != '!' and i != ':' and i != '?':
            new_word = i[1:] + i[0] + 'ay'
        else:
            new_word = i
        result.append(new_word)
    return ' '.join(result)


print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))
