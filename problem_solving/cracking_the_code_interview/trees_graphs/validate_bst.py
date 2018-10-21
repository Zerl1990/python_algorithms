# Validate BST: Implement a function to check if a binary tree is a binary search
# tree

import os
import sys
from tree_node import TreeNode, root

INT_MAX = 4294967296
INT_MIN = -4294967296

def is_binary_search_tree(root):
    return check_bst(root, INT_MIN, INT_MAX)

def check_bst(root, mini, maxi):
    if not root:
        return True

    if root.value < mini or root.value > maxi:
        return False
        
    return check_bst(root.left, mini, root.value - 1) and check_bst(root.right, root.value + 1, maxi)

        



if __name__ == '__main__':
    print is_binary_search_tree(root)
    
