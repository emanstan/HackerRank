#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    curMax = scores[0]
    curMin = scores[0]
    ret = [0, 0]
    for s in scores:
        if s > curMax:
            curMax = s
            ret[0] += 1
        if s < curMin:
            curMin = s
            ret[1] += 1
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
