# From an array, Need to find an index in which sum of left elements & sum of right elements are same.
# Simple approach, sum all, sum left until all/2
import os
import sys


def equilibrium_guide_solution(arr):
    total_sum = sum(arr)
    leftsum = 0
    for i, num in enumerate(arr):
        total_sum -= num
        leftsum += num
        if leftsum == total_sum:
            return i
    return -1
if __name__ == '__main__':
    arr = [2, 2, 2, 2, 2, 10]
    print equilibrium_guide_solution(arr)
