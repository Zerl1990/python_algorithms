# Palindrome: Implement a function to check if a linked list is a palindrome

import os
import sys
from Node import Node

def string_to_linked_list(string):
    head = None
    it = None
    string = string.lower().replace(" ", "")
    for index in xrange(len(string)):
        if not head:
            head = Node(string[index], None)
            it = head
        else:
            it.next = Node(string[index], None)
            it = it.next
    return head


def is_list_palindrome(head):
    stack = []
    
    # O (N)
    it = head
    while it:
        stack.append(it.value)
        it = it.next
    print stack
    
    # O (N)
    it = head
    while it:
        if stack.pop() != it.value:
            return False
        it = it.next
    return True
        

if __name__ == '__main__':
    palindrome = string_to_linked_list('Anita Lava La Tina')
    palindrome.print_list()
    print is_list_palindrome(palindrome)
    palindrome = string_to_linked_list('Luis Rivas')
    palindrome.print_list()
    print is_list_palindrome(palindrome)
    
