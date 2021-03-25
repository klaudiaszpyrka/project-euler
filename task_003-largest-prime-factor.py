# Project Euler+ challenge #3
# https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem

import math

test_cases = [-1, 0, 1, 2, 3, 10, 15, 600851475143]


def find_largest_prime_factor(number):
    
    if number < 2:
        print("Incorrect input")
        
    elif number == 2:
        return 2
    
    elif number % 2 == 0:
            return find_largest_prime_factor(number//2)
        
    else:    
        for i in range (3, math.ceil(math.sqrt(number+1)), 2):
            if number % i == 0:
                if number // i == 1:
                    return i                    
                else:
                    return find_largest_prime_factor(number//i)
        else:
            return number   


for test_case in test_cases:
    print(find_largest_prime_factor(test_case))
