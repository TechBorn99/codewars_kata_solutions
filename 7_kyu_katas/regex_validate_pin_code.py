"""
Kata description:

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly
6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""


def validate_pin(pin):
    return pin.isnumeric() and (len(pin) == 4 or len(pin) == 6)


if __name__ == "__main__":
    print(validate_pin("1234"))
    print(validate_pin("12345"))
    print(validate_pin("a234"))
