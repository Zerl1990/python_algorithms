#Minimal Tree: Given a sorted(Increasing order) array with unique integer elements wirte
# an algorithm to create a binary tree with minimal height
import os
import sys
from tree_node import TreeNode, root

def sorted_list_to_tree(numbers):
    middle = len(numbers) // 2
    root = None
    if middle >= 0 and middle < len(numbers):
        root = TreeNode(numbers[middle])
        root.left = sorted_list_to_tree(numbers[0:middle])
        root.right = sorted_list_to_tree(numbers[middle+1:])
    return root

if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8,9,10]
    print sorted_list_to_tree(numbers)
    
        


