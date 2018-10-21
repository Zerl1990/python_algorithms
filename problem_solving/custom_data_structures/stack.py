import os
import sys



class Stack(object):
    def __init__(self):
        self.items = []

    # Constant time
    def push(self, item):
        self.items.append(item)

    # Remove contest time
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return 'QUEUE: ' + '->'.join(str(item) for item in self.items)


s = Stack()
s.push(1)
s.push(2)
s.push('3')
while not s.empty():
    print s.pop()
