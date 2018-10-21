# Is Unique: Implement an algorithm to determine if a string
# has all unique characters.
# Cannot use additional data structures
import os
import sys


def is_unique(string):
    # O(n)
    string = string.lower().strip().replace('\s', '')

    # O(n*log*n)
    string = sorted(string)

    # O(n)
    prev_char = string[0]
    for char in string[1:]:
        if char == prev_char:
            return False
        else:
            prev_char = char

    # Complexity is O(n*log*n)
    return True

if __name__ == '__main__':
    print is_unique('Hello World!')
    print is_unique('Luis')
