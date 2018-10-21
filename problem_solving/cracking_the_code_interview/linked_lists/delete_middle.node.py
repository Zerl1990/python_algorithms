# Delete Middle Node: Implement an algorithm to delete a node in the middle
# a single linked list, given only access to that node. (Specific to remove)
import os
import sys
import math
from Node import head

# 1->2->3->4->5->2->3->4->5
def remove_middle_element_auto_find(head):
    # O(N)
    middle = int(math.ceil(get_size(head) / 2.0))
    count = 1
    it = head
    # O(N/2)
    while it and count < middle - 1:
        print it.value
        it = it.next
        count += 1
    #O(C)
    to_delete = it.next
    it.next = to_delete.next
    to_delete.next = None

def remove_middle_element(target):
    next_node = target.next

    # update value of target to next node
    target.value = next_node.value

    # remove
    target.next = next_node.next
    next_node.next = None
    
        
def get_size(head):
    count = 0
    it = head
    while it:
        count += 1
        it = it.next
    return count

if __name__ == '__main__':
    head.print_list()
    #remove_middle_element_auto_find(head)
    remove_middle_element(head.next.next.next)
    head.print_list()
