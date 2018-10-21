# Return Kth to Last: Implement an algorithm to find the kth
# to last element of single linked list
import os
import sys
from Node import head

# 1->2->3->4->5->2->3->4->5
def find_last_k_element(head, k):
    if head == None:
        return 1
    else:
        lvl = find_last_k_element(head.next, k)
        if lvl == k:
            print 'FOUND: {0}'.format(head.value)
        return lvl + 1
        


if __name__ == '__main__':
    head.print_list()
    find_last_k_element(head, 2)
    head.print_list()

