# Run length encoding
# aaaaaabb -> a5b2
# aaaaabccc -> a5bc3
import os
import sys

def encode(string):
    count = 1
    c_char = string[0]
    
    for char in string[1:]:
        if char == c_char:
            count = count + 1
        else:
            yield '{0}{1}'.format(c_char, count)
            count = 1
            c_char = char

    yield '{0}{1}'.format(c_char, count)


for string in ["aaaaaabb", "aaaaabccc"]:
    print string
    print ''.join(encode(string))
    print '-' * 80
