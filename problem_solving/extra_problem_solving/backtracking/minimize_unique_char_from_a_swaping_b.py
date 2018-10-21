# Given two strings A and B. Minimize the number of unique characters in string A by either swapping A[i] with B[i] or keeping it unchanged. The number 
# of swaps can be greater than or equal to 0. Note that A[i] can be swapped only with same index element in B. Print the minimum number of unique 
# characters. Constraints: 0 < length of A = 15.

import os
import sys

# Constraints
#	Size > 0
#	Swap should be same index
#		Are A and B same Size
#	Backtracking rule, take char, if unique count is greater keep it, if not go back

def get_max_value(string):
	return len(string) + 1

def min_unique(a,b):
	minimun = get_unique_count(a)
	swap_index = 0
	return _min_unique(a,b, swap_index, minimun)
	
def _min_unique(a, b, swap_index, minimun):
	tmp_a = list(a)
	tmp_a[swap_index] = b[swap_index]
	count = get_unique_count(tmp_a)
	
	if count > minimun:
		return minimun

	new_min = count
	for pos in xrange(swap_index+1, len(a)):
		new_min = min(new_min, _min_unique(tmp_a, b, pos, new_min))
	return new_min
		
	
def get_unique_count(string):
	return len(set(string))

A = 'abcedf'
B = 'ddccxx'

print min_unique(list(A), list(B))