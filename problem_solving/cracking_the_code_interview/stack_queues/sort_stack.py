# Sort Stack: Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but may not copy the elements into any other data
# structure.

import os
import sys
from stack import Stack

class SortedStack(object):
    def __init__(self):
        self.stack = Stack()
        self.support_stack = Stack()

    def push(self, item):
        if self.stack.empty():
            self.stack.push(item)
        else:
            while not self.stack.empty() and self.stack.peek() < item:
                self.support_stack.push(self.stack.pop())

            self.stack.push(item)
            while not self.support_stack.empty():
                self.stack.push(self.support_stack.pop())
                

    def pop(self):
        return self.stack.pop()

    def empty(self):
        return self.stack.empty()



if __name__ == '__main__':
    stack = SortedStack()
    stack.push(1)
    stack.push(2)
    stack.push(10)
    stack.push(5)
    stack.push(1)
    stack.push(11)
    while not stack.empty():
        print stack.pop()
    
    
