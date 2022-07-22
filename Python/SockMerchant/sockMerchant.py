#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    leftovers = {}
    p = 0
    for i in ar:
        #print(i)
        if not i in leftovers:
            leftovers[i] = 0
            #print("added ", i)
        if (leftovers[i] + 1) % 2 == 0:
            p += 1
            leftovers[i] = 0
            #print("added 1 pair to", i)
        else:
            leftovers[i] += 1
    return p

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
