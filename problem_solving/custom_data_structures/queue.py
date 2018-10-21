import os
import sys



class Queue(object):
    def __init__(self):
        self.items = []

    # Constant time
    def add(self, item):
        self.items.append(item)

    # Remove contest time
    def pull(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return 'QUEUE: ' + '->'.join(str(item) for item in self.items)


q = Queue()
q.add(1)
q.add(2)
q.add('3')
while not q.empty():
    print q.pull()
