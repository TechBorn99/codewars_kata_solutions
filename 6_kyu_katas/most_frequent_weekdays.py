"""
Kata description:

What is your favourite day of the week? Check if it's the most frequent day of the week in the year.

You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year. The
result has to be a list of days sorted by the order of days in week (e. g. ['Monday', 'Tuesday'],
['Saturday', 'Sunday'], ['Monday', 'Sunday']). Week starts with Monday.

Input: Year as an int.

Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).

Preconditions:

Week starts on Monday.
Year is between 1583 and 4000.
Calendar is Gregorian.
Example:

most_frequent_days(2427) == ['Friday']
most_frequent_days(2185) == ['Saturday']
most_frequent_days(2860) == ['Thursday', 'Friday']
"""


import datetime
import calendar


def most_frequent_days(year):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    num_of_days = [52 for i in range(7)]

    first_day_of_year = -1
    first_day = datetime.datetime(year, month=1, day=1).strftime("%A")

    for i in range(7):
        if first_day == days[i]:
            first_day_of_year = i

    if calendar.isleap(year):
        num_of_days[first_day_of_year] += 1
        num_of_days[(first_day_of_year + 1) % 7] += 1

    else:
        num_of_days[first_day_of_year] += 1

    li = [days[x] for x in range(7) if num_of_days[x] == 53]
    return li


print(most_frequent_days(2427))
print(most_frequent_days(2185))
print(most_frequent_days(2860))
