# Given n-ary tree. zigzag level order traversal
#           1
#       2           3
#   4       5   6       7
#
# Output: 1-2-3-7-6-5-4
#
# Constraints:
#   Binary Tree?
#   Balanced Tree?
#   Order of zig zag (Controll it?)

import os
import sys

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Modification of breath first
def print_zig_zag(root):
    stack_1 = [root]
    stack_2 = []
    while stack_1 or stack_2:
        while stack_1:
            cur = stack_1.pop()
            print cur.data
            if cur.right:
                stack_2.append(cur.right)
            if cur.left:
                stack_2.append(cur.left)
        while stack_2:
            cur = stack_2.pop()
            print cur.data
            if cur.left:
                stack_1.append(cur.left)
            if cur.right:
                stack_1.append(cur.right)
        
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print_zig_zag(root)
# Tcs:
# None, Unbalanced Tree
