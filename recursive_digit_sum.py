#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def recursive(n, k):
    if int(n) * k < 10:
        return int(n) * k
    
    new_n = 0
    for num in n:
        new_n += int(num)
    
    new_n *= k
    
    return recursive(str(new_n), 1)

def superDigit(n, k):
    return recursive(n, k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
