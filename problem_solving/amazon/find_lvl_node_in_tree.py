# Given Binary Tree, find level of x node if x is present otherwise return 0.
import os
import sys

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right =right

def find_node_lvl(root, goal, lvl=1):
    if not root:
        return 0
    
    if root.value == goal:
        return lvl
    
    tmp = find_node_lvl(root.left, goal, lvl+1)
    if tmp != 0:
        return tmp
    else:
        return find_node_lvl(root.right, goal, lvl+1)
    

if  __name__ == '__main__':
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(11)
    root.left.right = Node(12)
    root.right.left = Node(21)
    root.right.right = Node(22)
    print find_node_lvl(root, 22)

    
