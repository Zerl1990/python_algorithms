##Given a Binary Search Tree (BST), modify it so
##that all greater values in the given BST are added
##to every node. For example, consider the following BST.
import sys
import os

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right =right

def reverse_in_order(root, total=0):
    if root.right:
        total = reverse_in_order(root.right, total)

    total = root.value + total 
    print total
    
    if root.left:
        total = reverse_in_order(root.left, total)

    return total

    
    


if  __name__ == '__main__':
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)
    reverse_in_order(root)
