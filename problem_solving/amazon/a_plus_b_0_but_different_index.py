##Given a 1D Array. Return True if there exists an element where a[i]+a[j] = 0 && i!=j.
##Reference : https://www.geeksforgeeks.org/find-a-pair-with-the-given-difference/
##
##Input : arr = {2,-3,4,1,-6,-4,1}
##Output : True
##
##Input : arr = {2,3,4,1,-6,4,1}
##Output : False

import sys
import os


def solve(arr):
    # 2N
    complements = [-1 * x for x in arr]
    print len(set(arr) & set(complements)) > 0

if __name__ == '__main__':
    solve([2, -3, 4, 1, -6, -4, 1])
    solve([2,3,4,1,-6,4,1])
        
