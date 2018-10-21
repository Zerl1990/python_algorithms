# -*- coding: cp1252 -*-
#Given an array,find the maximum j – i such that arr[j] > arr[i]
import random

def get_best_start_candidates(arr):
    mininum = arr[0]
    candidates = [0]
    for index in xrange(1, len(arr)):
        if arr[index] < mininum:
            mininum = arr[index]
            candidates.append(index)
    return candidates[::-1]
            

arr = [random.randint(1,100) for num in range(10)]
st_candidates = get_best_start_candidates(arr)

j = len(arr) - 1
max_distance = 0
while j > 0:
    if j not in st_candidates:
        for i in st_candidates:
            if arr[j] > arr[i] and j - i > max_distance:
                print "Updating max distance {0} - {1}".format(j, i)
                max_distance = j - i
            elif arr[j] <= arr[i]:
                break
    j =- 1
                

print "Original arr: {0}".format(arr)
print "Canidates indexes: {0}".format(st_candidates)
print "Max distance: {0}".format(max_distance)
