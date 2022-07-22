#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #print(n, p, "mid-point =", n / 2)
    if p > n / 2:
        #print("from back")
        if n % 2 == 0:
            n += 1
        return int((n - p) / 2)
    else:
        #print("from front")
        return int(p / 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
