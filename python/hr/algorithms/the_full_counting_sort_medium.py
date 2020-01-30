#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
  max_val = -1
  for i in range(len(arr)):
    arr[i][0] = int(arr[i][0])
    if i < len(arr) // 2:
      arr[i][1] = '-'
    max_val = max(max_val, arr[i][0])
  
  counts = [0 for _ in range(max_val + 1)]
  for i in arr:
    counts[i[0]] += 1
  for i in range(1, len(counts)):
    counts[i] += counts[i-1]
  
  out = ['' for _ in range(len(arr))]
  for i in arr[::-1]:
    out[counts[i[0]] - 1] = i[1]
    counts[i[0]] -= 1
  
  print(' '.join(out))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
