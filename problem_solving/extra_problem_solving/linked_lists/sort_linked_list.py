# Sort a linked list in O(n log n) time using constant space complexity.
# Merge sort
# https://www.geeksforgeeks.org/merge-sort-for-linked-list/

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sort(head):
    if not head or not head.next:
        return
    first_half, second_half = split_list_by_half(head)
    sort(first_half)
    sort(second_half)
    temp = merge(first_half, second_half)
    head = temp

def split_list_by_half(head):
    slow = head
    fast = head.next
    while fast:
        fast = fast.next
        if fast:
            slow = slow.next
            fast = fast.next    
    first_half =  head
    second_half = slow.next
    slow.next = None
    return (first_half, second_half)

def merge(a,b):
    temp = None
    if a is None:
        return b
    if b is None:
        return a
    if a.data <= b.data:
        temp = a
        temp.next = merge(a.next, b)
    else:
        temp = b
        temp.next = merge(a, b.next)
    return temp
            
def print_list(head):
    to_print = []
    while head:
        to_print.append(str(head.data))
        head = head.next
    print '->'.join(to_print)
        
head = Node(6)
it = head
it.next = Node(22)
it = it.next
it.next = Node(33)
it = it.next
it.next = Node(4)
it = it.next
it.next = Node(35)
it = it.next
it.next = Node(61)
it = it.next
it.next = Node(7)
it = it.next

print_list(head)
sort(head)
print_list(head)
