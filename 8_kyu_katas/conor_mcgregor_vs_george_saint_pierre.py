"""
Kata description:

This is a beginner friendly kata especially for UFC/MMA fans.

It's a fight between the two legends: Conor McGregor vs George Saint Pierre in Madison Square Garden. Only one
fighter will remain standing, and after the fight in an interview with Joe Rogan the winner will make his legendary
statement. It's your job to return the right statement depending on the winner!

If the winner is George Saint Pierre he will obviously say:

"I am not impressed by your performance."
If the winner is Conor McGregor he will most undoubtedly say:

"I'd like to take this chance to apologize.. To absolutely NOBODY!"
Good Luck!
"""


def quote(fighter):
    q1 = 'I am not impressed by your performance.'
    q2 = 'I\'d like to take this chance to apologize.. To absolutely NOBODY!'
    return q1 if fighter.lower() == 'george saint pierre' else q2


if __name__ == "__main__":
    print(quote('george saint pierre'))
    print(quote('conor mcgregor'))
    print(quote('George Saint Pierre'))
    print(quote('Conor McGregor'))
