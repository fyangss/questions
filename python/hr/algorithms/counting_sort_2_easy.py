#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
  freq = []
  for i in range(100):
    freq.append(0)
  for i in arr:
    freq[i] += 1

  out = []
  for i in range(len(freq)):
    if freq[i] != 0:
      for _ in range(freq[i]):
        out.append(i)

  return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
