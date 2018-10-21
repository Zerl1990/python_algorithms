# Partition: Write code to partition a linked list around a value x.
# such that all nodes less than x come before all nodes greater
# than or equal to x.
import os
import sys
from Node import head

# 1->2->3->4->5->2->3->4->5
def partition(head, partition):
    left_side = None
    right_side = None
    it = head
    r_head = None
    
    while it:
        next_node = it.next
        it.next = None

        # Append to a side of the list
        if it.value < partition:
            if left_side:
                left_side.next = it
                left_side = left_side.next
            else:   
                left_side = it
                head = left_side
        else:
            if right_side:
                right_side.next = it
                right_side = right_side.next
            else:
                right_side = it
                r_head = right_side

        it = next_node

    left_side.next = r_head
        


if __name__ == '__main__':
    head.print_list()
    partition(head, 5)
    head.print_list()
