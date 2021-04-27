"""
Kata description:

Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome! To celebrate,
you're taking your team out to the terrible dive bar next door and using the referral bonus to buy, and build, the
largest three-dimensional beer can pyramid you can. And then probably drink those beers, because let's pretend it's
Friday too.

A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second, 9 in the
next, 16, 25...

Complete the beeramid function to return the number of complete levels of a beer can pyramid you can make, given the
parameters of:

    1. your referral bonus, and

    2. the price of a beer can

For example:

beeramid(1500, 2); // should === 12
beeramid(5000, 3); // should === 16
"""


def beeramid(bonus, price_per_piece):
    if bonus <= 0:
        return 0

    total_price = 0
    i = 0
    num_of_levels = [0, i]

    while total_price <= bonus:
        i += 1
        num_of_levels[1] += i ** 2
        if num_of_levels[1] * price_per_piece > bonus:
            break
        total_price = num_of_levels[1] * price_per_piece
        num_of_levels[0] = i

    return num_of_levels[0]


if __name__ == "__main__":
    print(beeramid(1500, 2))
    print(beeramid(5000, 3))
