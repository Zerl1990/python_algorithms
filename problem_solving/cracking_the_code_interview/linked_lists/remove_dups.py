# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP:
#   How would you solve this problem if a temporary buffer is not allowed?
import os
import sys
from Node import head

# 1->2->3->4->5->2->3->4->5
def remove_duplicates(head):
    unique_numbers = set()

    it = head
    unique_numbers.add(it.value)

    # Always look into future
    while it.next:
        if it.next.value in unique_numbers:
            to_delete = it.next
            it.next = it.next.next
            to_delete.next = None
        else:
            unique_numbers.add(it.next.value)
            it = it.next
        


if __name__ == '__main__':
    head.print_list()
    remove_duplicates(head)
    head.print_list()

