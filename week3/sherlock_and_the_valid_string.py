#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    
    res = []
    for char in (set(s)):
        res.append(s.count(char))
    
    if len(res) == 1:
        return "YES"
    
    sor = sorted(res)
    change = sor[0] != sor[1]
    curr = sor[1]
    
    for ele in sor[1:]:
        if ele != curr:
            if change or abs(ele - curr) > 1:
                return "NO"
            change = True
    
            
    return "YES"
        
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

