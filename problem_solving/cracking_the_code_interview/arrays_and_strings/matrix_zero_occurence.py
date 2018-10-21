import os
import sys


def print_matrix(mtx):
    for row in xrange(len(mtx)):
        print ' '.join(str(num) for num in mtx[row])

def zero_occurence(mtx):
    # Get row and col candidates
    rows_to_change = set()
    cols_to_change = set()

    # O(N)
    for row in xrange(len(mtx)):
        for col in xrange(len(mtx[0])):
            if mtx[row][col] == 0:
                rows_to_change.add(row)
                cols_to_change.add(col)

    # Worst case O(N)
    for row in rows_to_change:
        for col in xrange(len(mtx[0])):
                mtx[row][col] = 0

    for col in cols_to_change:
        for row in xrange(len(mtx)):
            mtx[row][col] = 0

if __name__ == '__main__':
    mtx = [[0,2,3], [4,0,6], [7,8,9]]
    print_matrix(mtx)
    zero_occurence(mtx)
    print '*' * 80
    print_matrix(mtx)
