# Project Euler+ challenge #1
# https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem

test_cases = [1, 1000, 1000000000]


def find_max_divisible(number, divider):
    max_divisible = 1

    for i in range(number - 1, 0, -1):
        if i % divider == 0:
            max_divisible = i
            break
        else:
            i -= 1

    return max_divisible


def multiples_sum(n):
    max_3 = find_max_divisible(n, 3)
    max_5 = find_max_divisible(n, 5)
    max_15 = find_max_divisible(n, 15)

    '''
    Creating lists (below) works only for small numbers, otherwise takes up too much resources.
    '''
    # sum_3_list = [3 * i for i in range(1, int(max_3/3) + 1)]
    # sum_5_list = [5 * i for i in range(1, int(max_5/5) + 1)]
    # sum_15_list = [15 * i for i in range(1, int(max_15/15) + 1)]
    # result = sum_3_list + sum_5_list - sum_15_list

    '''
    Calculation based on common arithmetic sequence formula (below) results in float rounding errors for big numbers.
    '''
    # sum_3 = (1 + max_3/3) / 2 * max_3
    # sum_5 = (1 + max_5/5) / 2 * max_5
    # sum_15 = (1 + max_15/15) / 2 * max_15
    # result = int(sum_3 + sum_5 - sum_15)

    '''
    We have to manipulate the arithmetic sequence formula to benefit from integer division.
    This ensures there are no rounding errors.
    '''
    sum_3 = (3 * max_3 + max_3 ** 2) // (2 * 3)
    sum_5 = (5 * max_5 + max_5 ** 2) // (2 * 5)
    sum_15 = (15 * max_15 + max_15 ** 2) // (2 * 15)

    result = int(sum_3 + sum_5 - sum_15)
    return result


for test_case in test_cases:
    print(multiples_sum(test_case))