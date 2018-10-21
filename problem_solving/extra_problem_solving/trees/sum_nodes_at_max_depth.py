import os
import sys

class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


    def __str__(self):
        if not self.left and not self.right:
            return str(self.value)
       
        string = str(self.left)
        string = string + '-' + str(self.value) + '-'
        string = string + str(self.right)
        return string


def depth(root):
    if not root:
        return 0
    return 1 + max(depth(root.left), depth(root.right))

# O(N)
def max_depth_sum(root):
    k = depth(root)
    return sum_k_level(root, k)

def sum_k_level(root, k):
    if not root:
        return 0
    if k == 1:
        return root.value
    return sum_k_level(root.left, k - 1) + sum_k_level(root.right, k - 1)

# Root
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)


# Second childs
it = root.left
it.left = TreeNode(4)
it.right = TreeNode(5)

it = root.right
it.left = TreeNode(6)
it.right = TreeNode(7)

# Constraints
# Not balanced tree
# Test cases:
#    Input:
#       empty root
#       node with non numeric values
#       node with negative numeric values
#       tree with only left subtrees or right
#       pass any non tree as root
#       tree of size 1
#   Cycles:
#       Tree with cycle
#       
print max_depth_sum(root)
