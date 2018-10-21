import os
import sys


# How to do it more pythonic
# How to handle different data types
# Which methods to override
class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

# Benefit of using head/tail
class List(object):
    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.it = None
        self.length = 0
        for arg in args:
            self.add(arg)

    # Insertion time O(C)
    def add(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next_node = Node(data)
            self.tail = self.tail.next_node
            self.length = self.length + 1

    # Remove time O(C)
    def pull(self):
        if self.head:
            tmp = self.head
            self.head = self.head.next_node
            tmp.next_node = None
            self.length = self.length - 1
            return tmp.data
        else:
            return None

    # Returns iterable, in this case self reference
    def __iter__(self):
        self.it = self.head
        return self

    # Next required for iterables, in python 3 is __next__
    # Should throw stop iteration when end is reached
    # We are using an internal variable to store the it
    def next(self):
        try:
            data = self.it.data
            self.it = self.it.next_node
            return data
        except Exception:
            raise StopIteration

    # O(C)    
    def __len__(self):
        return self.length

    # O(N)
    def __str__(self):
        return '->'.join(str(item) for item in self)



# Corner cases
#       List intialization:
#           Empty list
#           List with only none values
#           List with dictionary or any non valid
#       Iteration:
#           In middle of iteration add/remove item (It's allowed?)
#       Add/Remove:
#           Test if length variable is changed
#       List with head tail:
#           Good for queue implementation, easy to add and remove
#           Good for stack implementation, easy to add and remove and growth
my_list = List(1,2,3,4,5,6,7,8)
for data in my_list:
    print data

print my_list

            
        
