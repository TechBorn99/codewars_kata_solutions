"""
Kata description:

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be
separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
"""


def namelist(names):
    result = ''
    if len(names) == 1:
        result = names[0]['name']
    elif len(names) == 2:
        result = '{} & {}'.format(names[-2]['name'], names[-1]['name'])
    elif len(names) > 2:
        result = ', '.join([d['name'] for d in names[:-2]]) + ', {} & {}'.format(names[-2]['name'], names[-1]['name'])
    return result


print(namelist([]))
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
