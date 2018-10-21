# Rotate Matrix: Give an image represented by an NxM matrix,
# where each pixel in the image is 4 bytes, write a method
# to rotate the image by 90 degrees. Can you do it in place?
import os
import sys

def print_image(mtx):
    for row in xrange(len(mtx)):
        row_str = ''
        for col in xrange(len(mtx[row])):
            row_str = row_str + ' ' + str(mtx[row][col])
        print row_str

def rotate_image(mtx):
    width = len(mtx[0])
    height = len(mtx)
    copy = [[0,0,0,0], [0,0,0,0], [0,0,0,0]] 
    for row in xrange(len(mtx)):
        for col in xrange(len(mtx[row])):
            rotate_row = col
            rotate_col = width - row
            copy[rotate_row][rotate_col] = int(mtx[row][col])    
    print_image(copy)
            
if __name__ == '__main__':
    img = [[1,2,3],
           [4,5,6],
           [7,8,9],
           [10,11,12]]
    print_image(img)
    print '*' * 80
    rotate_image(img)
