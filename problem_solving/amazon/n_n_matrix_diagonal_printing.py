# Given a matrix of n*n size, the task is to print its elements in diagonally pattern.
import os
import sys

def print_diagonal(arr):
    diagonal_indexes = [(0, col) for col in xrange(len(arr[0]))][::-1] + [(row, 0) for row in xrange(1, len(arr))]
    for row, col in diagonal_indexes:
        print_diagonal_line(arr, row, col)

def print_diagonal_line(arr, row, col):
    max_col = len(arr[0])
    max_row = len(arr)
    while col < max_col and row < max_row:
        print arr[row][col]
        col += 1
        row +=1

if __name__ == '__main__':
    arr = [[1,2,3],
           [4,5,6],
           [7,8,9],
           [10,11,12]]
    print_diagonal(arr)
