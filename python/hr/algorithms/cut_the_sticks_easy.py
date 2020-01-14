#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
  ans = []
  while len(arr) != 0:
    ans.append(len(arr))
    min_stick = min(arr)
    arr = list(filter((min_stick).__ne__, arr))
    for i in range(len(arr)):
      arr[i] -= min_stick

  return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

