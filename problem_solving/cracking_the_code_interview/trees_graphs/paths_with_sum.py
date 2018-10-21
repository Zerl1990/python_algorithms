# Paths with sums: You are given a binary tree in which each node has a integer
# positive or negative, design an algorithm to count the number of paths that
# sum N number
import os
import sys
from tree_node import TreeNode, root

def get_paths(root, N, path):

    # Leaf, return just the value
    if not root:
        return 0

    # Check if it's a path
    path.append(root.value)

    # Get count from left sub tree
    left_count = get_paths(root.left, N, path)
    
    # Get count from right sub tree
    right_count = get_paths(root.right, N, path)

    # Check if we can get the sum
    is_subpath = sub_arr(path, N)

    # Delete current node
    path.pop()
    
    return is_subpath + left_count + right_count
    
def sub_arr(arr, N):
    total_sum = sum(arr)

    if total_sum == N:
        return 1
    elif total_sum < N:
        return 0
    else:
        for index in xrange(len(arr) - 1):
            sub_sum = total_sum - arr[index]
            
            if sub_sum == N:
                return 1

            if sub_sum < N:
                break;
        return 0
        

if __name__ == '__main__':
    print get_paths(root, 3, [])
    
    
        


