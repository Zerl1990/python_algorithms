###  Lazy Bartender
## There are N number of possible drinks.(n1,n2..)
## Has C number of fixed customers.
## Every customer has fixed favorite set of drinks.
## Bartender has to create least possible number of drinks to suffice need of all the customers
## Example:
##  Cust1: n3,n7,n5,n2,n9
##  Cust2: n5
##  Cust3: n2,n3
##  Cust4: n4
##  Cust5: n3,n4,n3,n5,n7,n4
##
## Output: 3(n3,n4,n5)


if __name__ == '__main__':
    c1 = set([3, 7, 5, 2, 9])
    c2 = set([5])
    c3 = set([2, 3])
    c4 = set([4])
    c5 = set([3,4,3,5,7,4])

    total = c1.union(c2).union(c3).union(c4).union(c5)
    favorite = dict(zip(total, [0] * len(total)))

    for c in [c1,c2,c3,c4,c5]:
        for d in c:
            favorite[d] = favorite[d] + 1
    print favorite
    favorite = sorted(favorite, key=favorite.get, reverse=True)
    print favorite

    
    
    
