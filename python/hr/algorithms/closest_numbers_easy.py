#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the closestNumbers function below.
def closestNumbers(arr):
  arr.sort()
  diffs = defaultdict(list)

  m = float('inf')
  for i in range(1, len(arr)):
    val = arr[i] - arr[i-1]
    m = min(m, val)
    diffs[val].append([arr[i-1], arr[i]])

  diffs[m].sort()
  out = []
  for i in diffs[m]:
    out += i
  
  return out


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
