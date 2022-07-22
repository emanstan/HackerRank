#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    ms = -1
    keyboards.sort(reverse=True)
    kbFiltered = list()
    for i in keyboards:
        if i > b:
            continue
        kbFiltered.append(i)
    drives.sort(reverse=True)
    dvFiltered = list()
    for j in drives:
        if j > b:
            continue
        dvFiltered.append(j)
    for i in kbFiltered:
        for j in dvFiltered:
            if i + j > b or i + j <= ms:
                continue
            ms = i + j
    return ms

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
