#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    num = 0
    for i in range(1, 101):
        allFactors = True
        aFactor = True
        #print("i =", i)
        for n in a:
            #print("  n =", n, "i % n =", i % n)
            if i % n != 0:
                allFactors = False
                #print("  False")
                break
        for m in b:
            #print("  m =", m, "m % i =", m % i)
            if m % i != 0:
                aFactor = False
                #print("  False")
                break
        num += (allFactors and aFactor)
        #print(i, (allFactors & aFactor), num)
    return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
