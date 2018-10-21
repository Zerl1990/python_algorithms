# https://www.google.com/search?q=pascal+triangle&rlz=1C1GGRV_enUS751US751&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj5kKGYip_aAhWLAnwKHcv3ChEQ_AUICigB&biw=1920&bih=949
import os
import sys


def print_pascal(rows=None):
    if rows == 0:
        return [1]
    prev_pascal =  print_pascal(rows-1)
    mid_elements = [1]
    for index in xrange(len(prev_pascal) - 1):
        mid_elements.append(prev_pascal[index] + prev_pascal[index+1])
    mid_elements.append(1)
    return mid_elements

# TC:
#   N: Very BIG
#   REcursive or loop
#   Improvements:
#       Loop
#       CACHE
print print_pascal(6)
