# Reverse linked list in groups of given k size
# Example:
# Inputs:  1->2->3->4->5->6->7->8->NULL and k = 3 
# Output:  3->2->1->6->5->4->8->7->NULL. 
#
# Inputs:   1->2->3->4->5->6->7->8->NULL and k = 5
# Output:  5->4->3->2->1->8->7->6->NULL.

import os
import sys


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class List(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add(self, value):
        self.count = self.count + 1
        if self.head == None:
            self.head = Node(value, None)
            self.tail = self.head
        else:
            self.tail.next = Node(value, None)
            self.tail = self.tail.next

    def add_all(self, values):
        if values:
            for val in values:
                self.add(val)

    def reverse_in_grps_of_k(self, k):
        sub_lists = []
        tmp_head = self.head
        iterator = self.head
        for index in xrange(self.count):
            if index > 1 and index % k == 0 or self.count - index  + 1 < k:
                new_head = self._reverse(tmp_head, k=k)
                sub_lists.append((new_head, tmp_head))
                tmp_head =  iterator
                last_reverse_index = index

            if self.count - index + 1  < k:
                break
            
            iterator = iterator.next

            

        self.head = sub_lists[0][0]
        self.tail = sub_lists[-1][1]

        prev_head = None
        prev_tail = None
        for head, tail in sub_lists:
            if prev_tail:
                prev_tail.next = head
            prev_tail = tail
            

    def reverse(self):
        new_head = self._reverse(self.head, k=self.count)
        self.tail = self.head
        self.head = new_head
        
    def _reverse(self, head, lvl = 1, k = 0):
        if head and lvl < k:
            new_head = self._reverse(head.next, lvl + 1, k)
            p2 = head.next
            if p2:
                p2.next = head
                head.next = None
                return new_head
            else:
                return head
        else:
            return head
            
            

    def __str__(self):
        tmp = self.head
        res_str = ''
        while tmp:
            if res_str:
                res_str = res_str + '->' + str(tmp.value)
            else:
                res_str = str(tmp.value)
            tmp = tmp.next
        return res_str


if __name__ == '__main__':
    my_list = List()
    my_list.add_all([1,2,3,4,5,6,7,8])
    print my_list
    my_list.reverse_in_grps_of_k(3)
    print my_list
