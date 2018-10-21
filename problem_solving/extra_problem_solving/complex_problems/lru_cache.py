# Least Recently Used
# Cache with some capacity
#   Track time to remove least used
# Get and Set should be O(1)
# Test page faults
# Test adding lot
# Test removing lot
import os
import sys


import collections

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
