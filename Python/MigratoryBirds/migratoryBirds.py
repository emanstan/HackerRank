#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    maxId = 5
    maxCnt = 0
    freq = [0,0,0,0,0]
    for i in arr:
        freq[5-i] += 1
    #print(freq)
    for i in range(5):
        #print(i, freq[i])
        if freq[i] >= maxCnt:
            maxId = 5-i
            maxCnt = freq[i]
    return maxId

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
