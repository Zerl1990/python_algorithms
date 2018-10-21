# Implement a MyQueue class which impelments a queue using two stacks

import os
import sys
from stack import Stack

class MyQueue(object):
    def __init__(self):
        self.stack_a = Stack()
        self.stack_b = Stack()

    def add(self, num):
        self.stack_a.push(num)

    def pull(self):
        if not self.stack_b:
            while self.stack_a:
                self.stack_b.push(self.stack_a.pop())
        return self.stack_b.pop()

if __name__ == '__main__':
    q = MyQueue()
    q.add(1)
    q.add(2)
    print q.pull()
    q.add(3)
    q.add(4)
    print q.pull()
