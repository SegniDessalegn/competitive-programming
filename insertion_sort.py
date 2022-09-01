#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    n -= 1
    right_most_element = arr[n]
    while True:
        if right_most_element > arr[n - 1] or n == 0:
            arr[n] = right_most_element
            for i in arr:
                print(i, end = " ")
            print()
            break
        else:
            arr[n] = arr[n - 1]
            for i in arr:
                print(i, end = " ")
            print()
        if n == 0:
            break
        n -= 1

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
