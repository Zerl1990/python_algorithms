import os
import sys

class Queue(object):
    def __init__(self)
        self.items = []

    def add(self, item)
        self.items.append(item)

    def pull(self, item)
        if item:
            return self.items.pop(0)
        else:
            return None
