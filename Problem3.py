#Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def problem_3():
    num = 9
    print (prime_check(num))


def prime_check(num):
    if num < 2:
        return False
    if num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
            else:
                return True
    
problem_3()
