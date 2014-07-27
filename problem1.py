#Problem 1: 
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def problem_1():   
    allMulitplesOf3 = set(range(0,1000,3))
    allMulitplesOf5 = set(range(0,1000,5))
    joinedSets = allMulitplesOf3.union(allMulitplesOf5)
    result = sum(joinedSets)

    print(result)

    
problem_1()

    
#Originally my solution check every number up to 1000 and checked to see if they could
#be divided by either 3 or 5, if it could that number was added to the result.  This new solution is more
#efficient as it generates two sets, one of all multiples of 3 and one of all multiples of 5.  These sets
#are then merged using 'union' and added together to give the result.
