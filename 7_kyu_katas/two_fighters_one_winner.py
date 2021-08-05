"""
Kata description:

Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as
having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the
Fighter objects.

Example:
class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__
"""


def declare_winner(fighter1, fighter2, first_attacker):
    i = 1
    winner = ''
    first = fighter1 if fighter1.name == first_attacker else fighter2
    second = fighter1 if fighter2.name == first_attacker else fighter2
    battle_over = False
    while not battle_over:
        if i % 2 == 1:
            second.health -= first.damage_per_attack
        else:
            first.health -= second.damage_per_attack
        if first.health <= 0 or second.health <= 0:
            winner = first.name if second.health <= 0 else second.name
            battle_over = True
        i += 1
    return winner
