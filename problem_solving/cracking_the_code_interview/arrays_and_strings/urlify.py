# URLify: Write a method to replace all spaces in a string with '%20'
# You may assume that has sufficient space at the to hold the addition characters
# and you are given the length of the string.
import os
import sys

# In place subsitution
def urlify(string):
    ls_string = list(string.lower())
    index = 0
    
    # O (N): Worst case
    while index < len(ls_string):
        if ls_string[index] == ' ':
            shift_content(ls_string, index + 1, 2)
            ls_string[index] = '%'
            ls_string[index+1] = '2'
            ls_string[index+2] = '0'
            index += 3
        else:
            index += 1
    
    return ls_string


def shift_content(string, offset, k):
    st_index = offset
    end_index = len(string) -1

    # O(N)
    while string[end_index] == ' ' and end_index >= st_index:
        end_index = end_index - 1

    # O (N)
    while end_index >= st_index:
        string[end_index + k] = string[end_index]
        string[end_index] = ''
        end_index = end_index - 1
    
    

if __name__ == '__main__':
    print urlify("luis rivas roger    ")
