# Intersection: Given two (single) linked lists, determine if the two
# lists intersects. Returns the intersecting node.
# Node that the intersection is defined based on reference, not value.
# that is, if the kth node of the first linked list is the exact soame node
# as the jt node of the second linked list, then they are intersectin

import os
import sys
from Node import Node

def find_intersection(head_A, head_B):
    size_A = get_size(head_A)
    size_B = get_size(head_B)
    diff = abs(size_A - size_B)

    if size_A > size_B:
        head_A = move_head(head_A, diff)
    else:
        head_B = move_head(head_B, diff)
    
    while head_A and head_B:
        head_A = head_A.next
        head_B = head_B.next
        if head_A == head_B:
            return head_A.value
    
    return None

def get_size(head):
    it = head
    size = 1
    while it:
        size += 1
        it = it.next
    return size

def move_head(head, k):
    count = 0
    while count < k:
        head = head.next
        count += 1
    return head
        

if __name__ == '__main__':
    head_A = Node('1A', None)
    it = head_A

    # Create first list - A
    it.next = Node ('2A', None)
    it = it.next
    it.next = Node ('3A', None)
    it = it.next
    it.next = Node ('4A', None)
    it = it.next
    intersection = it
    
    it.next = Node ('5A', None)
    it = it.next
    it.next = Node ('6A', None)
    it = it.next
    it.next = Node ('7A', None)
    it = it.next
    it.next = Node ('8A', None)
    it = it.next

    # Create second list - B
    head_B = Node('1B', None)
    it = head_B

    it.next = Node ('2B', None)
    it = it.next
    it.next = Node ('3B', None)
    it = it.next
    it.next = Node ('4B', None)
    it = it.next

    # Intersect
    it.next = intersection

    head_A.print_list()
    head_B.print_list()
    print find_intersection(head_A, head_B)
    
