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
def freqDict(d,i):
  if i in d:
    d[i] += 1
  else:
    d[i] = 1

def getNum(d,i):
  if i in d:
    return d[i]
  return 0

def pickingNumbers(a):
  freq = {}
  for i in a:
    freqDict(freq,i)

  max_val = 0
  for i in freq:
    max_val = max(max_val, freq[i] + getNum(freq,i+1))
  return max_val


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

