"""
Kata description:

The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. Given a lowercase
string that has alphabetic characters only (both vowels and consonants) and no spaces, return the length of the longest
vowel substring. Vowels are any of aeiou.

Good luck!
"""


def solve(s):
    value = 0
    for i in range(len(s)):
        j = i
        st = ''
        while s[j] in 'aeiou':
            st += s[j]
            j += 1
            if j == len(s):
                break

        if value < len(st):
            value = len(st)

    return value


if __name__ == "__main__":
    print(solve("codewarriors"))
    print(solve("suoidea"))
    print(solve("ultrarevolutionariees"))
    print(solve("strengthlessnesses"))
    print(solve("cuboideonavicuare"))
    print(solve("chrononhotonthuooaos"))
    print(solve("iiihoovaeaaaoougjyaw"))
