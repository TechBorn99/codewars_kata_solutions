"""
Kata description:

In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you
have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
The order of the permutations doesn't matter.
"""
import itertools


def permutations(string):
    permutations_list = []
    character_sequences = itertools.permutations(string)

    for sequence in set(character_sequences):
        string_permutation = "".join(sequence)
        permutations_list.append(string_permutation)

    return permutations_list


print(permutations('a'))
print(permutations('ab'))
print(permutations('aabb'))
