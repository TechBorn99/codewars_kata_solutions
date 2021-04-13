"""
Kata description:

Debugging sayHello function
The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard.
It is your job to fix the code and get the program working again!

Example output:

Hello, Mr. Spock
"""


def say_hello(name):
    return "Hello, " + name


if __name__ == "__main__":
    print(say_hello('Mr. Spock'))
    print(say_hello('Captain Kirk'))
    print(say_hello('Liutenant Uhura'))
    print(say_hello('Dr. McCoy'))
    print(say_hello('Mr. Scott'))
