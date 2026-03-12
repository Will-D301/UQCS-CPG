#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    total = len(arr)
    p = n = z = 0
    for ele in arr:
        if ele > 0:
            p += 1
        elif ele < 0:
            n += 1
        else:
            z += 1
    print(f"{p / total}\n{n/total}\n{z/total}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

