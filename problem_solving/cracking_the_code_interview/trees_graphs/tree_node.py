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

