# Rotate Doubly Linked List by N time
# NULL <= a =><= b =><= c =><= d =><= e =><= f =><= g =><= h => NULL
# Given Num: 4
# O/P:
# NULL <= e =><= f =><= g =><= h =><= a =><= b =><= c =><= d => NULL

import sys
import os

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

def print_list(node):
    while node:
        print node.value
        node = node.next

def rotate_list(head, n):
    count = 0
    current = head

    # Get Kth node
    while current and count < n:
        current = current.next
        count = count + 1
    kth_node = current

    

    # Check if we are the end
    if not current:
        return
    
    # Go to end
    while current.next:
        current = current.next

    # Create circle list
    current.next = head
    head.prev = current

    # break list where we want
    kth_node.prev.next = None
    kth_node.prev = None
    return kth_node
    
    

if __name__ == '__main__':
    head = Node('a')
    it = head
    for char in ['b', 'c', 'd', 'e', 'f', 'g', 'h']:
        it.next = Node(char)
        it.next.prev = it
        it = it.next
    
    print_list(rotate_list(head, 4))
