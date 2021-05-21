"""
Kata description:

Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling
faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

Example
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
Note
In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of
the face (eyes, nose, mouth) elements will always be the same.
"""


def count_smileys(arr):
    result = 0
    for i in arr:
        if i[0] == ':' or i[0] == ';':
            if i[len(i) - 1] == ')' or i[len(i) - 1] == 'D':
                if len(i) > 2 and (i[1] == '-' or i[1] == '~'):
                    result += 1
                elif len(i) == 2:
                    result += 1
    return result


print(count_smileys([':)', ';(', ';}', ':-D']))
print(count_smileys([';D', ':-(', ':-)', ';~)']))
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))
