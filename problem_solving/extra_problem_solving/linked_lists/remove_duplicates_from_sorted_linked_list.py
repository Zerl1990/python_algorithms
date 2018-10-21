# Take sorted linked list and remove all duplicates
import os
import sys

class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

def print_list(head):
    it = head
    elements = []
    while it:
        elements.append(str(it.value))
        it = it.next_node
    print '->'.join(elements)

def remove_duplicates(head):
    prev_step = head
    next_step = prev_step

    # O(N) - Traversal
    while next_step:

        # Find jump
        while next_step and (prev_step == next_step or prev_step.value == next_step.value):
            tmp = next_step
            next_step = next_step.next_node
            tmp.next_node = None
        
        # Connect prev to next
        prev_step.next_node = next_step

        # Swap variables
        prev_step = next_step
        next_step = prev_step
        
    

head = Node(1)
tmp = head
tmp.next_node = Node(1)
tmp = tmp.next_node
tmp.next_node = Node(1)
tmp = tmp.next_node
tmp.next_node = Node(2)
tmp = tmp.next_node
tmp.next_node = Node(3)
tmp = tmp.next_node
tmp.next_node = Node(4)
tmp = tmp.next_node
tmp.next_node = Node(5)
tmp = tmp.next_node
tmp.next_node = Node(5)
tmp = tmp.next_node
print_list(head)
remove_duplicates(head)
print_list(head)

# Test cases:
# Input Type:
#   No numeric
#   Negative
#   Objects
# Size of Input:
#   None/Small/Med/Large
# Order of input:
#   Repeated at begging
#   All repeated
#   Repetead at the end
#   Repeated in the middle
# Cycles:
#   Loop in linked list

