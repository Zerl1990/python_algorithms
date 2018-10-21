# Check Permutations: Given two strings write a method to
# device if one is a permutation of the other
import os
import sys
import string

def is_permutation(a, b):
    alp = [0] * 26
    a = a.lower()
    b = b.lower()

    # a ascii value
    a_ascii = ord('a')
    
    # O(N)
    for char in a:
        alp[ord(char) - a_ascii] += 1

    # O(N)
    for char in b:
        alp[ord(char) - a_ascii] -= 1

    # Final complexity: O(N)
    return (sum(alp) == 0)

if __name__ == '__main__':
    
    print is_permutation('dlroW', 'World')
    print is_permutation('luis', 'roger')
