##The cost of a stock on each day is given in an array, find the max
##profit that you can make by buying and selling in those days.
##For example, if the given array is {100, 180, 260, 310, 40, 535, 695},
##the maximum profit can earned by buying on day 0, selling on day 3.
##Again buy on day 4 and sell on day 6.
##If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.
import os
import sys


if __name__ == '__main__':
    stocks = [100, 180, 260, 310, 40, 535, 695]

    # get best start canidates
    start_points = [0]
    min_left_cost = stocks[0]
    for index in xrange(len(stocks)):
        if stocks[index] < min_left_cost:
            min_left_cost = stocks[index]
            start_points.append(index)
    
    #Traverse in reverse and find max diff
    print "BEST START CANDIDATES: {0}".format(start_points)
    max_diff = 0
    end_index = len(stocks)
    
    while start_points:
        st_index = start_points.pop()
        index = st_index + 1
        while index < end_index:
            print "Comparing: {0} - {1}".format(stocks[index], stocks[st_index])
            tmp_diff = stocks[index] - stocks[st_index]
            print "Result: {0}".format(tmp_diff)
            if tmp_diff > max_diff:
                max_diff = tmp_diff
            index = index + 1
        end_index = st_index

    print max_diff
                
    
    
