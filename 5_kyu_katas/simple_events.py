"""
Kata description:

Your goal is to write an Event constructor function, which can be used to make event objects.

An event object should work like this:

it has a .subscribe() method, which takes a function and stores it as its handler
it has an .unsubscribe() method, which takes a function and removes it from its handlers
it has an .emit() method, which takes an arbitrary number of arguments and calls all the stored functions with
these arguments
As this is an elementary example of events, there are some simplifications:

all functions are called with correct arguments (e.g. only functions will be passed to unsubscribe)
you should not worry about the order of handlers' execution
the handlers will not attempt to modify an event object (e.g. add or remove handlers)
the context of handlers' execution is not important
each handler will be subscribed at most once at any given moment of time. It can still be unsubscribed and then
subscribed again
Also see an example test fixture for suggested usage
"""


class Event():

    def __init__(self):
        self.handlers = []

    def subscribe(self, handler):
        self.handlers.append(handler)

    def unsubscribe(self, handler):
        self.handlers.pop(self.handlers.index(handler))

    def emit(self, *args):
        for i in self.handlers:
            i(*args)


class Testf():
    def __init__(self):
        self.calls = 0
        self.args = []

    def __call__(self, *args):
        self.calls += 1
        self.args += args


if __name__ == "__main__":

    event = Event()
    f = Testf()

    event.subscribe(f)
    event.emit(1, 'foo', True)

    print(f.calls)
    print(f.args)

    event.unsubscribe(f)
    event.emit(2)

    print(f.calls)
