"""
Kata description:

You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:

the second and the last letter is switched (e.g. Hello becomes Holle)
the first letter is replaced by its character code (e.g. H becomes 72)
Note: there are no special characters used, only letters and spaces

Examples

decipherThis('72olle 103doo 100ya'); // 'Hello good day'
decipherThis('82yade 115te 103o'); // 'Ready set go'
"""


def decipher_this(string):
    temp = string.split(' ')
    result = []
    for i in temp:
        word = ''
        fl = ''
        for j in i:
            if j.isnumeric():
                fl += j
        word += chr(int(fl))
        tmp = [x for x in i if not x.isnumeric()]
        if len(tmp) >= 2:
            tmp[0], tmp[len(tmp) - 1] = tmp[len(tmp) - 1], tmp[0]
        word += ''.join(tmp)
        result.append(word)
    return ' '.join(result)


print(decipher_this('72olle 103doo 100ya'))
print(decipher_this('82yade 115te 103o'))
