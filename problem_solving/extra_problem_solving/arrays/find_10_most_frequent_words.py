# In a file there are 1 million words.
# Find 10 most frequent words in that file.
# Hint use a trie and min heap
import sys
import os
import collections

WordCounter = collections.namedtuple('WordCounter', ['word', 'count'])

words = ['day', 'sun', 'something', 'sun']

class MinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
        
    def insert (self, value):
        self.heap_list.append(value)
        self.current_size = self.current_size + 1
        self._percolate_up(self.current_size)

    def remove (self):
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]
        self.heap_list.pop()
        self.current_size -= 1
        self._percolate_down(1)
        return min_val

    def peek(self):
        return self.heap_list[1]
        
    def _percolate_up(self, root):
        while root // 2 > 0:
            if self.heap_list[root] < self.heap_list[root // 2]:
                tmp = self.heapList[root // 2]
                self.heapList[root // 2] = self.heapList[root]
                self.heapList[root] = tmp
            root = root // 2
        
    def _percolate_down(self, root):
        while root * 2  <= self.current_size:
            mc = self._min_child(root)
            if self.heap_list[root] > self.heap_list[mc]:
                tmp = self.heap_list[root]
                self.heap_list[root] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            root = mc

    def _min_child(self, root):
        left = root * 2
        right = left + 1
        if right > self.current_size:
            return left
        else:
            if self.heap_list[left] < self.heap_list[right]:
                return left
            else:
                return right

if __name__ == '__main__':
    words_count = {}
    minHeap = MinHeap()
    # Iterate and track words count
    # Update heap
    for word in words:
        if word not in words_count:
            words_count[word] = 1
        else:
            words_count[word] = words_count[word] + 1

        if minHeap.current_size < 10:
            minHeap.insert(words_count[word])
        elif minHeap.peek() < words_count[word]:
            minHeap.remove()
            minHeap.insert(words_count[word])
            
            
    while minHeap.current_size > 0:
        print minHeap.remove()
    
