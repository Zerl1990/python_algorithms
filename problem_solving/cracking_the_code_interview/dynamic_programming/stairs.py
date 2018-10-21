# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct
# ways can you climb to the top?
#
# 1: [1]
# 2: [1,1] [2]
# 3: [1,1,1] [2,1] [1,2]
# 4: [1,1,1,1] [2,1,1] [1,2,1] [1,1,2]  [2,2]
# 5: [1,1,1,1,1] [2,1,1,1] [1,2,1,1] [1,1,2,1] [1,2,2] [2,1,2] [2,2,1]
# 6: [1,1,1,1,1,1] [2,1,1,1] [


def ways_to_do_it(top):
    if top == 1:
        return 1
    elif top == 2:
        return 2
    else:
        return ways_to_do_it(top-1) + ways_to_do_it(top-2)

def ways_to_do_it_loop(top):
    res = [0 for x in xrange(top)]
    res[0] = 1
    res[1] = 2
    for index in xrange(2, top):
        res[index] = res[index-1] + res[index-2]
    return res[top-1]

top = 4
print ways_to_do_it_loop(top)
