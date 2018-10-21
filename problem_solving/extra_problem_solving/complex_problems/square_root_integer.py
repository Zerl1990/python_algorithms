# Given an integer x, find square root of it.
# If x is not a perfect square, then return floor(√x).
import os
import sys


def square_root(num):
    if num == 0 or num == 1:
        return num
    start = 1
    end = num
    ans =None

    while start <= end:
        mid = (end + start) // 2
        if mid*mid == num:
            return mid
        if mid*mid < num:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

    return ans
print square_root(8)
