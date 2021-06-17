from functools import total_ordering

@total_ordering
class GreatIndividual(object):
    ''' Great, but somehow malicious individual.
        Represents a number but is far more.
        One could say it has it's very own way of doing thing.
        Does not give too much about rules.'''

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        # we are all individuals
        return False

    def __ne__(self, other):
        return True # so true

    def __gt__(self, other):
        self.value = self.value + other.value
        # i am always the greatest
        return True

def individuals_until(limit):
    return [GreatIndividual(a) for a in range(limit)]

print(max(individuals_until(1000 + 1)).value)
