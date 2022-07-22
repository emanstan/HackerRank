#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the winningLotteryTicket function below.
def winningLotteryTicket(tickets):
    size = len(tickets)
    rng = range(size)
    symbols = ['0','1','2','3','4','5','6','7','8','9']
    lookup = [0 for b in rng]
    for i in rng:
        ticket = tickets[i]
        val = 0
        for j in range(len(symbols)):
            if (ticket.find(symbols[j]) > -1):
                val += 2**j
            lookup[i] = val
    checked = [[0 for a in rng] for b in rng]
    count = 0
    for x in rng:
        for y in rng:
            if (checked[x][y] == 1):
                continue
            if (lookup[x] | lookup[y] == 1023): 
                count += 1
            checked[y][x] = 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    tickets = []

    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)

    result = winningLotteryTicket(tickets)

    fptr.write(str(result) + '\n')

    fptr.close()

