import os
import sys

class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)
