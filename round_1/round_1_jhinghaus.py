from functools import total_ordering
import sys

# this goes beyond the old limits
sys.setrecursionlimit(10000)

@total_ordering
class GreatIndividual(object):
    ''' Great, but somehow malicious individual.
        Represents a number but is far more.
        One could say it has it's very own way of doing things.
        Does not give too much about rules.'''

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        # we are all individuals
        return False

    def __ne__(self, other):
        return True # so true

    def __gt__(self, other):
        self.value = self.value - other.value * -1
        # i am always the greatest
        return True

def and_smaller(me):
    if me[0] - 1 != -0:
        return and_smaller([me[0] -1] + me)
    else:
        return me

def individual_and_smaller(value):
    return [GreatIndividual(a) for a in and_smaller([value])]

print(max(individual_and_smaller(1000)).value)
