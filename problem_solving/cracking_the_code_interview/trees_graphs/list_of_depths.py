# List Of Depths: Given a binary tree, design and algorithm which creates a
# linked list of all hte nodes at each depths
import os
import sys
from tree_node import TreeNode, root

def list_of_depths(root, list_of_linked_lists, lvl=0):
    if len(list_of_linked_lists) < lvl + 1:
        list_of_linked_lists.append([])

    if root:
        list_of_linked_lists[lvl].append(root.value)

        list_of_depths(root.left, list_of_linked_lists, lvl+1)

        list_of_depths(root.right, list_of_linked_lists, lvl+1)

if __name__ == '__main__':
    list_of_linked_lists = []
    list_of_depths(root, list_of_linked_lists)
    print list_of_linked_lists
    
    
        


