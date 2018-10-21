# Check Balanced: Implement a function to check if a binary tree is balanced.
# For the purpose of this question, a balanced tree is defined to be a tree
# such that the heights of the two subtress of any node never differ by more than one


import os
import sys
from tree_node import TreeNode, root

def is_balanced(root):
    lh = depth(root.left)
    rh = depth(root.right)
    return abs(lh-rh) <= 1

def depth(root):
    if not root:
        return 0
    return max(depth(root.left), depth(root.right)) + 1


if __name__ == '__main__':
    print is_balanced(root)
    
