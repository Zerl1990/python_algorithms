import os
import sys

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        'Returns itself as an iterator object'
        return self

    # Python 3 is __next__
    def next(self):
        'Returns the next value till current is lower than high'
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

class Iterable:
    def __init__(self):
        pass
    def __iter__(self):
        return Counter(0, 10)

    
def generator():
    for i in range(10):
        "Genering next one"
        yield i


for i in generator():
    print "After next Generator"
    print i
