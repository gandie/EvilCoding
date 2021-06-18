'''TODO: write a manual'''
from abc import *  # we need all abc here
import sys  # import the system, too

A = sys.argv[1:]  # early args pickup!

class ItemBase(metaclass=ABCMeta):  # use metaclass to avoid mixin subclass struggle
    '''Item base class'''
    def __init__(self, data):
        self._data = data

    def check_data(self):
        '''checks the data. strings are best for data'''
        assert isinstance(self.data, str), 'Error: Bad data'

    @property  # keep real data a secret, do not expose attributes!
    def data(self):
        return self._data

    @abstractmethod
    def handle(self):  # implement in subclasses, remember to check data
        pass

class SequenceGenerator(ItemBase):
    '''a generator for sequences from just a single number'''
    def handle(self):
        '''handle the sequence generation'''
        assert isinstance(self.data, Number)  # special, attention: data must be a raw UNHANDLED number!
        self.data.handle()
        c = 1
        s = ''
        while c <= self.data._data:
            s += '{num} '.format(num=c)
            c += 1
        self._data = s  # set secret data to s

class Number(ItemBase):
    '''Numbers come here'''
    def handle(self):
        '''handle numbers correctly'''
        self.check_data()
        assert self.data.isdigit(), 'Can not handle data'
        self._data = int(self.data)

    def __add__(self, other):  # implement adding
        '''ATTENTION: only handled numbers will work! do NOT mix with unhandled'''
        assert isinstance(other, Number), 'NaN: Not a number'
        return Number(self.data + other.data)  # result is a number, too! no handling required

class NumberSequence(ItemBase):
    '''a sequence of numbers. a list of pre-handled numbers after handling'''
    def handle(self):
        '''handle a sequence of numbers'''
        self.check_data()  # remember to check data!!!!!
        sRaw = self._data.split()
        s = []
        for i in sRaw:
            n = Number(i)
            n.handle()  # handle data before saving!
            s.append(n)
        self._data = s

    def sum_up(self):
        '''sum up sequence numbers, assuming sequence is already handled'''
        start = Number('0')
        start.handle()
        for i in self.data:
            start += i
        return start.data

class Manager:
    '''the main manager'''
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    
    def main(self):
        '''the main mehtod'''
        assert not self.kwargs, 'do NOT use kwargs!'
        num = self.args[0]
        num = Number(num)
        seq = SequenceGenerator(num)
        seq.handle()
        seq = NumberSequence(seq.data)
        seq.handle()
        print(seq.sum_up())

m = Manager(*A)

try:
    m.main()
except:
    print('Error.')
    print('Usage: python round_1_gandie.py <number>')
    print('<number> must be like 1, 2, 3, ...')
