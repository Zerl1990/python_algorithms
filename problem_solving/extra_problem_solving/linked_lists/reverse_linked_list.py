import os
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(current_node):
    next_node = current_node.next
    if not next_node:
        return current_node

    new_head = reverse(next_node)
    current_node.next = None
    next_node.next = current_node
    return new_head

def print_reverse(current):
    if not current:
        return
    print_reverse(current.next)
    print current.data

def print_list(head):
    to_print = []
    it = head
    while it:
        to_print.append(str(it.data))
        it = it.next
    print '->'.join(to_print)
    
head = Node(1)
it = head
it.next = Node(2)
it = it.next
it.next = Node(3)
it = it.next
it.next = Node(4)
it = it.next
it.next = Node(5)
it = it.next
print_list(head)
print_reverse(head)
#it = reverse(head)
#print '*' * 80
#print_list(it)
