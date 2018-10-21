# Reverse single linked list
# 1->2->3->4->5->6
#
import os
import sys

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
		
		
def print_list(head):
    while head:
        print head.value
        head = head.next

def reverse_list(p1):
    if not p1:
        return p1
    p2 = reverse_list(p1.next)
    p1.next = None
    # Reverse
    if not p2:
        tail = p1
    if p2 and p1:
        p2.next = p1
    return p1
        

# https://www.geeksforgeeks.org/reverse-a-linked-list/

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
    it.next = Node(6, None)
    tail = it.next
    print_list(head)
    reverse_list(head)
    print '*' * 80
    print_list(tail)
