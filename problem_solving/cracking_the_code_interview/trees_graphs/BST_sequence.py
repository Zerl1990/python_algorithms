# A binary search tree was created by traversing thorugh an array
# from left to right and inserting each element.
# Given a binary search tree with distinct elements print all possible
# arrays that could have led to this tree.
import os
import sys

# [2,5,6,3,1,7]

class Node:  
    # Constructor to create a new tree node
    def __init__(self, key):
        self.key = key 
        self.left = None
        self.right = None

def find_sequence(root):
    list_of_levels = []
    _find_seq(root, list_of_levels, 0)
    # Do combinations of sub elements
    return '*'.join('-'.join(row) for row in list_of_levels)

def _find_seq(root, list_of_levels, lvl=0):
    if root:
        if len(list_of_levels) <= lvl:
            list_of_levels.append([])
        list_of_levels[lvl].append(root.key)
        _find_seq(root.left, list_of_levels, lvl+1)
        _find_seq(root.right, list_of_levels, lvl+1)

    
# Let us create a binary tree given in the above example
root = Node('8')
root.left = Node('6')
root.right = Node('10')
root.left.left = Node('4')
root.left.right = Node('7')
root.right.left = Node('9')
root.right.right = Node('11')

print find_sequence(root)
