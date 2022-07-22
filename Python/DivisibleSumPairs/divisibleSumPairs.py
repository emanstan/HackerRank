#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    c = 0
    for j in range(0, n):
        i = 0
        while i < j:
            #print("(",i,",",j,") ", ar[i], ar[j], k, " v =", (ar[i] + ar[j]) % k)
            c += (ar[i] + ar[j]) % k == 0
            i += 1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
