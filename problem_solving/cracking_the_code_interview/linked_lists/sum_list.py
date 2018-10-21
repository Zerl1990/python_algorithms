# Sum Lists: You have two numbers represented by a linked list, where
# each node contains a single digit. The digit are stored in reverse order,
# such that the 1's digit is at the head fo the list. Write a
# function that adds the two numbers and returns the sum as a linked list

import os
import sys
from Node import Node

# 1->2->3->4->5->2->3->4->5

def number_to_linked_list(number):
    head = None
    it = None
    while number > 0:
        if not head:
            head = Node(number % 10, None)
            it = head
        else:
            it.next = Node(number % 10, None)
            it = it.next
        number = number // 10
    return head
        
def list_to_number(head):
    number = 0
    multiplier = 1
    it = head
    while it:
        number = number +  it.value * multiplier
        multiplier = multiplier * 10
        it = it.next
    return number

if __name__ == '__main__':
    l1 = number_to_linked_list(1982)
    l2 = number_to_linked_list(100)
    n1 = list_to_number(l1)
    n2 = list_to_number(l2)
    result = n1 - n2
    lr = number_to_linked_list(result)
    lr.print_list()
