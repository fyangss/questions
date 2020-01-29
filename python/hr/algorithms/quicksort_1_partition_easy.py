#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
  out = []
  pivot = []
  right = []
  for i in arr:
    if i < arr[0]:
      out.append(i)
    elif i == arr:
      pivot.append(i)
    else:
      right.append(i)
  out += pivot + right
  return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
