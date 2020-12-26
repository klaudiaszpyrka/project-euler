# Project Euler+ challenge #2
# https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem

test_cases = [10, 100, 4000000]


def even_fibonacci_sum(n):
    fibonacci = [1, 2]
    i = 0

    while True:
        i = fibonacci[-1] + fibonacci[-2]
        if i > n:
            break
        else:
            fibonacci.append(i)

    return sum([i for i in fibonacci if i % 2 == 0])


for test_case in test_cases:
    print(even_fibonacci_sum(test_case))
