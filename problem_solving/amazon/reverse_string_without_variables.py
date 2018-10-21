# How to find all boundary node of a tree.
import os
import sys

string = "Luis Rivas"

def reverse(string):
    count = len(string)
    while count:
        count = count -1
        yield string[count]
        

if __name__ == '__main__':
    print ''.join(reverse(string))
