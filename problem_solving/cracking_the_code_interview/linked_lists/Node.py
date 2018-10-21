import os
import sys


class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def print_list(self):
        string = str(self.value)
        it = self.next
        while it:
            string = string + '->' + str(it.value)
            it = it.next
        print string




head = Node(1, None)
it = head
for num in xrange(2,6):
    it.next = Node(num, None)
    it = it.next

for num in xrange(2,6):
    it.next = Node(num, None)
    it = it.next
