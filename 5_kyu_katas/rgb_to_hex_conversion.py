"""
Kata description:

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must
be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""


def convert(code):
    if code <= 255:
        if code >= 0:
            converted_code = hex(code).replace('x', '')
            if len(converted_code) != 2:
                converted_code = converted_code.replace('0', '')
            elif len(converted_code) < 2:
                converted_code += '0'
        else:
            converted_code = '00'
    else:
        converted_code = 'FF'
    return converted_code


def rgb(r, g, b):
    result = []
    for i in [r, g, b]:
        result.append(convert(i))
    return ''.join([x.upper() for x in result])


print(rgb(255, 255, 255))
print(rgb(255, 255, 300))
print(rgb(0, 0, 0))
print(rgb(148, 0, 211))
