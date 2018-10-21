# Stack of plates: Imagine a literal stack of plates.
# If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack
# when the previous stack exceeds some threshold. Implement a data
# structure SetOfStacks that mimic this.
import os
import sys
from stack import Stack


class StackOfPlates(object):
    def __init__(self, max_capacity=10):
        self.stacks = []
        self.stacks.append(Stack())
        self.cur = 0
        self.max_capacity = max_capacity

    def push(self, num):
        if len(self.stacks[self.cur]) == self.max_capacity:
            self.stacks.append(Stack())
            self.cur += 1

        self.stacks[self.cur].push(num)

    def pop(self):
        if len(self.stacks[self.cur]) == 0:
            self.cur -= 1
            self.stacks.pop()
        return self.stacks[self.cur].pop()

    def __str__(self):
        string = ''
        for stack in self.stacks:
            string = string + '\n' + ' '.join(str(item) for item in stack.items)
        return string


if __name__ == '__main__':
    stacks = StackOfPlates(2)
    stacks.push(1)
    stacks.push(2)
    stacks.push(3)
    stacks.push(4)
    stacks.push(5)
    print stacks
    stacks.pop()
    stacks.pop()
    print stacks
    
