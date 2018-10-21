# Construct node from inorder traversal
# TCS:
#   None data
#   No Childs
#   Only one child
#   No numeric
# Is completed?, is balanced?

import os
import sys
import math

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def deserialize(string):
    k = math.log(len(string)+1, 2)
    root = Node(string.pop(0))
    _deserialize(string, root, k-1)
    return root

def _deserialize(string, root, k):
    # Go up to keep serializing in order way
    if k < 1:
        return
    root.left = Node(string.pop(0))
    _deserialize(string, root.left, k - 1)
    root.right = Node(string.pop(0))
    _deserialize(string, root.right, k - 1)
    

def print_tree_in_order(root):
    if root:
        print root.data
        print_tree_in_order(root.left)
        print_tree_in_order(root.right)


string = '1245367'
root = deserialize(list(string))
print_tree_in_order(root)
