# Convert a binary tree to its sum tree(each node is the sum of its children)
import os
import sys

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def print_tree_in_order(root):
    if root:
        print root.value
        print_tree_in_order(root.left)
        print_tree_in_order(root.right)

# In order traversal
def convert(root, seen=None):
    if not seen:
        seen = set()     
    if not root or root in seen:
        return 0
    else:
        child_sum = convert(root.left, seen.add(root)) + convert(root.right, seen.add(root))
        node_value = root.value
        root.value = child_sum
        return node_value + child_sum

root = Node(10)
root.left = Node(-2)
root.right = Node(6)
root.left.left = Node(8)
root.left.right = Node(-4)
root.right.left = Node(7)
root.right.right = Node(5)
print_tree_in_order(root)
print '-' * 80
convert(root)
print_tree_in_order(root)
print '-' * 80
# Constraints:
#   Binary tree?
#   Balanced tree?
#   Only numeric? negative values?
#   Sum node with child values?
#
# TCS:
#   None root
#   Only one child
#   Only right or left subtree
#   Loops
#
#
#




























