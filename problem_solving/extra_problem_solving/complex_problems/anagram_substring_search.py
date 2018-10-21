# Given a text txt[0..n-1] and a pattern pat[0..m-1],
# write a function search(char pat[], char txt[])
# that prints all occurrences of pat[] and
# its permutations (or anagrams) in txt[]. You may assume that n > m. 
# Expected time complexity is O(n)
#
#
#1) Input:  txt[] = "BACDGABCDA"  pat[] = "ABCD"
#   Output:   Found at Index 0
#             Found at Index 5
#             Found at Index 6
#2) Input: txt[] =  "AAABABAA" pat[] = "AABA"
#   Output:   Found at Index 0
#             Found at Index 1
#             Found at Index 4
import os
import sys

MAX = 256
 
def compare(arr1, arr2):
    for i in range(MAX):
        if arr1[i] != arr2[i]:
            return False
    return True
     
def search(pat, txt):
 
    M = len(pat)
    N = len(txt)
    countP = [0] * MAX
    countTW = [0] * MAX
 
    for i in range(M):
        countP[ord(pat[i])] += 1
        countTW[ord(txt[i])] += 1
 
    for i in range(M,N):
        if compare(countP, countTW):
            print("Found at Index", (i-M))
        countTW[ord(txt[i])] += 1
        countTW[ord(txt[i-M])] -= 1
       
    if compare(countP, countTW):
        print("Found at Index", N-M)

search('ABCD', 'BACDGABCDA')
print '*' * 80
search('AABA', 'AAABABAA')

