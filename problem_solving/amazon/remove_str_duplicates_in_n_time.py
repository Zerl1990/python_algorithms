# Remove duplicates from string in place in O(n).
# Can use helpers?
# 
import os
import sys

def remove_duplicates(string):
    alp = set()
    index = 0
    while index < len(string):
        jump = 1
        if string[index] in alp:
            jump = remove_char(string, index, alp)
        alp.add(string[index])
        index += jump
    return string

def remove_char(string, index, alp):
    next_valid = index + 1

    # Find next valid jump
    while next_valid < len(string) and string[next_valid] in alp:
        next_valid += 1

    jump = next_valid - index
    
    # Swap until next valid
    if next_valid < len(string):
        tmp = string[index]
        string[index] = string[next_valid]
        string[next_valid] = tmp
        return 1
    else:
        # We didn't find next valid, swap everything till end
        while index < next_valid:
            string[index] = None
            index += 1
        return jump

# Test cases:
# Type of Input:
#   None
#   Non string
#   String with non alpha
#   Very big string
#   Other object, iterator
# Size on input:
#   Small
#   Medium
#   Large
#   Order of input
#   Repeated caracters until last one
#   Repeted character in the middle
#   Repeeated charaters in the ned

string = 'Hello Hello World'
string = list(string.lower().strip().replace(' ', ''))
print remove_duplicates(string)
string = 'Hello'
string = list(string.lower().strip().replace(' ', ''))
print remove_duplicates(string)
