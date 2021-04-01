"""
Kata description:
Complete the function circleArea so that it will return the area of a circle with the given radius. Round the returned
number to two decimal places (except for Haskell). If the radius is not positive or not a number, return false.

Example:
circleArea(-1485.86)     #returns False
circleArea(0)            #returns False
circleArea(43.2673)      #returns 5881.25
circleArea(68)           #returns 14526.72
circleArea("number")     #returns False
"""


from math import pi


def circle_area(r):
    try:
        return round(r ** 2 * pi, 2) if r > 0 else False
    except:
        return False


if __name__ == '__main__':

    print(circle_area(-1485.86))
    print(circle_area(0))
    print(circle_area(43.2673))
    print(circle_area(68))
    print(circle_area("number"))
