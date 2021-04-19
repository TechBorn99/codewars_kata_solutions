"""
Kata description:

An NBA game runs 48 minutes (Four 12 minute quarters). Players do not typically play the full game, subbing in and out
as necessary. Your job is to extrapolate a player's points per game if they played the full 48 minutes.

Write a function that takes two arguments, ppg (points per game) and mpg (minutes per game) and returns a straight
extrapolation of ppg per 48 minutes rounded to the nearest tenth. Return 0 if 0.

Examples:

nba_extrap(12, 20) # 28.8
nba_extrap(10, 10) # 48
nba_extrap(5, 17) # 14.1
nba_extrap(0, 0) # 0
Notes:
All inputs will be either be an integer or float.
Follow your dreams!
"""


def nba_extrap(ppg, mpg):
    return 0 if ppg == 0 else round(ppg * (48 / mpg), 1)


if __name__ == "__main__":
    print(nba_extrap(12, 20))
    print(nba_extrap(10, 10))
    print(nba_extrap(5, 17))
    print(nba_extrap(0, 0))
