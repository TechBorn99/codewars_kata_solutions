"""
Kata description:

Build Tower
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
JavaScript: returns an Array;
C#: returns a string[];
PHP: returns an array;
C++: returns a vector<string>;
Haskell: returns a [String];
Ruby: returns an Array;
Lua: returns a Table;
Have fun!

for example, a tower of 3 floors looks like below

[
  '  *  ',
  ' *** ',
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ',
  '    ***    ',
  '   *****   ',
  '  *******  ',
  ' ********* ',
  '***********'
]

"""


def tower_builder(n):
    tower = []
    for i in range(1, n + 1):
        num_of_stars = i * 2 - 1
        num_of_spaces = (n * 2 - num_of_stars) // 2
        row = ''
        row += ' ' * num_of_spaces
        row += '*' * num_of_stars
        row += ' ' * num_of_spaces
        tower.append(row)
    return tower


for row in tower_builder(6):
    print(row)