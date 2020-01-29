#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
  swaps = 0
  # Insertion Sort 2
  for i in range(1, len(arr)):
    for j in range(i-1, -1, -1):
      if arr[j] > arr[j+1]:
        arr[j+1], arr[j] = arr[j], arr[j+1]
        swaps += 1
  return swaps
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
