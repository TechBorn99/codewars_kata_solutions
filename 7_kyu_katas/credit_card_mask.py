"""
Kata description:

maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"
"""


def maskify(cc):

    if len(cc) < 4:
        return cc
    else:
        cc1 = ''
        for i in range(len(cc) - 4):
            cc1 += '#'
        cc1 += cc[len(cc) - 4:]
        return cc1


if __name__ == "__main__":
    print(maskify("4556364607935616"))
    print(maskify(     "64607935616"))
    print(maskify(               "1"))
    print(maskify("Nananananananananananananananana Batman!"))