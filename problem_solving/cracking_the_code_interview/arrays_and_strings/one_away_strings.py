# One away: There are three types of edits that can be performed on strings
# inser, remove or replace. Given two strings, write a function to check if
# they are one edit (or zero edits) away.
import os
import sys


def one_away(str_a, str_b):
    len_diff = abs(len(str_a) - len(str_b))
    if len_diff > 0:
        return True
    else:
        # O(N)
        return are_strings_diffs(str_a, str_b)

def are_strings_diffs(str_a, str_b):
    alp = {}

    # O(N)
    for char in str_a:
        if char in alp:
            alp[char] = alp[char] + 1
        else:
            alp[char] = 1

    # O(N)
    for char in str_b:
        if char in alp:
            alp[char] = alp[char] - 1

    # O(N)
    total = sum(abs(val) for key,val in alp.items())
    return (total < 2)
        

if __name__ == '__main__':
    print one_away('pale', 'ple')
    print one_away('pales', 'pale')
    print one_away('pale', 'bale')
    print one_away('pale', 'bake')
