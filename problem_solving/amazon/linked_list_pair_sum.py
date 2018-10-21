# Linked List pair sum count
# 0 -> 2 -> 5 -> 7 -> 4 -> 6 -> 10 -> 20 -> -10 -> Null
# Given Sum: 10
# Output : 3
# Explanation: (4, 6) (0, 10) (20, -10)
import sys
import os
import collections

class Node:
    def __init__(self, next, value):
        self.next = next
        self.value = value

def print_list(node):
    print node.value
    if node.next:
        print_list(node.next)

def find_pair_sum(node, goal):
    targets = []
    total_pairs = 1
    while node:
        if node.value in targets:
            targets.remove(node.value)
            total_pairs += 1
        else:
            targets.append(goal - node.value)
        node = node.next
    return total_pairs

if __name__ == '__main__':
    head = Node(None, 0)
    iterator = head
    for value in [2,5,7,4,6,10,20,10]:    
        iterator.next = Node(None, value)
        iterator = iterator.next
    print find_pair_sum(head, 10)
   
