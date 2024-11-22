# read the input.txt file

file = open("input.txt", "r").read()

import math


def last_runner_standing(n):
    # Find the largest power of 2 less than or equal to n
    largest_power_of_2 = 2 ** int(math.log2(n))
    # Calculate the position of the last remaining runner
    return 2 * (n - largest_power_of_2) + 1


n = 103785
result = last_runner_standing(n)
print(result)
