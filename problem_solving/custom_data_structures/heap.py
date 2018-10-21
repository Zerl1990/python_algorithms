import os
import sys

# Heap satisfy this condition:
#   * If P is a parent node of C, then the key of P is either greater than
#     or equal to (max heap) or less than or equal to (min heap) the key of
#     C.
#
# Queue is one maximally efficient implementation of an abstract data type
# called Priority Queue, priority queues are often referred as heaps.
# Binary heap, only two childs per node.
#
# Implementation is a complete binary tree
#
# Use the custom compare method of each store item, can be modify to create a
# min or max heap
class Heap(object):
    def __init__(self):
        # Leave first element empty to simplify calculation
        # and work better with indexes
        self.items = [0]
        self.length = 0

    # Worst case O(N)
    def insert(self, *args):
        for arg in args:
            self.items.append(arg)
            self.length += 1
            self.percolate_up(self.length)

    # Worst case O(N)
    def remove(self):
        if self.length < 2:
            self.length -= 1
            return self.items.pop()
        else:
            # Store item to return
            top_item = self.items[1]

            # Pop last element to maintain structure
            last_element = self.items.pop()

            # Move poped element to root
            self.items[1] = last_element
        
            self.length -= 1
            self.percolate_down(1)
            return top_item

    # Worst case O(N)
    def percolate_up(self, curr):
        while curr > 1:
            parent = self._get_parent(curr)
            if self.compare(curr, parent):
                self.swap(curr, parent)
                curr = parent
            else:
                break

    # Worst case O(N)
    def percolate_down(self, curr):
        while curr < self.length:
            min_child = self.get_min_child(curr)
            if min_child and self.items[curr] > self.items[min_child]:
                self.swap(curr, min_child)
                curr = min_child
            else:
                break    

    def peek(self):
        return self.items[1]
    
    # Swap elements, constant time
    def swap(self, index_a, index_b):
        tmp = self.items[index_a]
        self.items[index_a] = self.items[index_b]
        self.items[index_b] = tmp

    # Isolate comparison part, constant time
    def compare(self, index_a, index_b):
        return self.items[index_a] < self.items[index_b]

    # Constant timpe
    def get_min_child(self, index):
        left = index * 2 
        right = index * 2 + 1
        
        # No childs
        if left > self.length or right > self.length:
            return None

        # Only one child
        if right > self.length:
            return left

        # Two child case
        if self.items[left] < self.items[right]:
            return left
        else:
            return right

    def _get_parent(self, index):
        return index // 2

    def __len__(self):
        return self.length

# Test Cases:
# * Input:
#       - add non numeric
#       - add negative numbers
#       - add same number multiple times
#       - add objects
# * remove:
#       - add/remove same element multiple times
#       - add 10 numbers, and finally add one number smaller to all of then (Test full cycle)
#       - add 10 numbers, add a very big value (Bottom), remove top and see what happend)
#
# *
# *
my_heap = Heap()
my_heap.insert(8,7,2,10,3,4)
while len(my_heap) > 0:
    print my_heap.remove()
        
