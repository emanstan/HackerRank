#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    run = [] #matches day
    sumRun = 0 #matches month
    c = 0
    for i in s:
        run.append(i)
        sumRun += i
        while sumRun > d or len(run) > m:
            sumRun -= run.pop(0)
        if sumRun == d and len(run) == m:
            c += 1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
