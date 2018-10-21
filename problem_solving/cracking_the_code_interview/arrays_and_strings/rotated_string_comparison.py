import os
import sys

def are_the_same(a,b):
    if len(a) != len(b):
        return False

    # O (N)
    st_candidates = []
    for index in xrange(len(b)):
        if b[index] == a[0]:
            st_candidates.append(index)

    # Check if we have the first caracter
    if not st_candidates:
        return False

    # O(ST)
    # Rotate string
    while st_candidates:
        st_index = st_candidates.pop()
        tmp = b[st_index:] + b[0:st_index]
        if tmp == a:
            return True
    return False


if __name__ == '__main__':
    a = 'lluiss'
    b = 'uissll'
    print are_the_same(a,b)
