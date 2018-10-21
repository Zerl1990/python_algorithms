# Remove Alternate Duplicate characters from a char array,
# you have to do it in Place.
# Like keeping only the odd occurences of each character.
import os
import sys
import string

# String to analyze
string = "Today is the day".lower()

def remove_duplicates(string):
    alp = {}
    for char in string:
        if char in alp:
            alp[char] = alp[char] + 1
        else:
            alp[char] = 1

        if alp[char] % 2 != 0:
            yield char

print ' '.join(remove_duplicates(string))
