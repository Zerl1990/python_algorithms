# -*- coding: cp1252 -*-
# Minimum removals from array to make max – min <= K
# Given N integers and K, find the minimum number of
# elements that should be removed such that Amax-Amin<=K.
# After removal of elements, Amax and Amin is considered
# among the remaining elements.
#
#
#Input : a[] = {1, 3, 4, 9, 10, 11, 12, 17, 20} 
#          k = 4 
#Output : 5 
#Explanation: Remove 1, 3, 4 from beginning 
#and 17, 20 from the end.
#
#Input : a[] = {1, 5, 6, 2, 8}  K=2
#Output : 3
#Explanation: There are multiple ways to 
#remove elements in this case.
#One among them is to remove 5, 6, 8.
#The other is to remove 1, 2, 5 


def min_removals(arr, k):
    arr_s = sorted(arr)
    return _min_removals(arr_s, k)

def _min_removals(arr, k):
    if len(arr) < 1:
        return 0
    elif arr[-1] - arr[0] <= k:
        return 0
    else:
        return 1 + min(_min_removals(arr[1:], k), _min_removals(arr[:-1], k))
    


arr = [1,3,4,9,10,11,12,17,20]
print min_removals(arr, 5)

arr = [1,5,6,2,8]
print min_removals(arr, 2)
