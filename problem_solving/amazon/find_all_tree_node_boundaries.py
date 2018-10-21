# How to find all boundary node of a tree.
# Leaft should be printed
# How to get left boundary
# How to get right boundary
import os
import sys

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right =right

def print_leaves(root):
    if root:
        print_leaves(root.left)
        if not root.left and not root.right:
            print root.value
        print_leaves(root.right)

def print_left_boundaries(root):
    if root:
        if root.left:
            print root.value
            print_left_boundaries(root.left)

        elif root.right:
            print root.value
            print_right_boundaries(root.right)

            

def print_right_boundaries(root):
    if root:
        if  root.right:
            print root.value
            print_right_boundaries(root.right)

        elif root.left:
            print root.value
            print_left_boundaries(root.left)

def print_boundaries(root):
    print root.value
    print_left_boundaries(root.left)
    print_leaves(root.left)
    print_leaves(root.right)
    print_right_boundaries(root.right)
        

if  __name__ == '__main__':
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(11)
    root.left.right = Node(12)
    root.right.left = Node(21)
    root.right.right = Node(22)
    print print_boundaries(root)
