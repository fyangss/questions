#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
  last_seen_index = {}
  min_dist = float('inf')
  for i in range(len(a)):
    if a[i] in last_seen_index:
      min_dist = min(min_dist, i - last_seen_index[a[i]])
      last_seen_index[a[i]] = i
    else:
      last_seen_index[a[i]] = i
  return min_dist if min_dist != float('inf') else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
