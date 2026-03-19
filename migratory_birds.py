#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    bc = Counter(arr)
    m = 0
    mb = 0
    for bird in arr:
        if bc[bird] > m:
            mb = bird
            m = bc[bird]
        elif bc[bird] == m:
            mb = min(bird, mb)
    
    return mb

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

