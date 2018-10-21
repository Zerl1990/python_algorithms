# Palindrome Permutation: Given a string, write a function to check if it is a
# permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a re-arrangment of letters. The palindrome does not need
# to be limited to just a dictionary of words.
# Example:
# Input: Tact Coa
# Output: True (permutation(taco cat, atco cta, etc)
import os
import sys

def is_palindrome_permutation(string):
    if len(string) <= 3:
        return False
    else:
        return True


if __name__ == '__main__':
    print is_palindrome_permutation('tact coa')
    
