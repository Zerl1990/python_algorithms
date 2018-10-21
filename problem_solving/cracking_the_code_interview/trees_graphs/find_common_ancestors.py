# Find common ancestor: Design an algorithm and write code to find the first
# common ancestor of two nodes in a binary search tree. Avoid storing additional
# nodes in a data structures. NOTE (It's not necessarily a BST)
import os
import sys

class Node:  
    # Constructor to create a new tree node
    def __init__(self, key):
        self.key = key 
        self.left = None
        self.right = None


def findLCA(root, n1, n2):
    if not root:
        return None

    if root.key == n1 or root.key == n2:
        return root

    l_lca = findLCA(root.left, n1, n2)
    r_lca = findLCA(root.right, n1, n2)

    if l_lca and r_lca:
        return root
    else:
        return l_lca if l_lca else r_lca



# Let us create a binary tree given in the above example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print "LCA(4,5) = ", findLCA(root, 4, 5).key
print "LCA(4,6) = ", findLCA(root, 4, 6).key
print "LCA(3,4) = ", findLCA(root, 3, 4).key
print "LCA(2,4) = ", findLCA(root, 2, 4).key
