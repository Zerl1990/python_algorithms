# Loop: Given a circular linked list, implement an algorithm that returns
# the node at the beginning of the loop

import os
import sys
from Node import Node


def find_circular_dependency(head):
    slow = head
    fast = head.next

    while slow and fast:
        if slow == fast:
            return slow.value
        slow = slow.next
        fast = fast.next.next
    return None

if __name__ == '__main__':
    head = Node(1, None)
    it = head
    
    it.next = Node(2, None)
    it = it.next

    it.next = Node(3, None)
    it = it.next

    it.next = Node(4, None)
    it = it.next

    it.next = Node(5, None)
    it = it.next

    it.next = head
    
    print find_circular_dependency(head)
    
