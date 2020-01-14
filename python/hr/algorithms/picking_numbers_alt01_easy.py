#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
  freq = []
  for i in range(0,100):
    freq.append(0)
  for i in a:
    freq[i] += 1

  max_sub = 0
  for i in range(len(freq)-1):
    max_sub = max(max_sub, freq[i]+freq[i+1])
  return max_sub


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

