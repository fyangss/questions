#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
  freq_map = {}
  for i in arr:
    if i in freq_map:
      freq_map[i] += 1
    else:
      freq_map[i] = 1

  max_sights = float('-inf')
  min_id = []
  for k in freq_map:
    if freq_map[k] > max_sights:
      max_sights = freq_map[k]
      min_id = [k]
    elif freq_map[k] == max_sights:
      min_id.append(k)

  return min(min_id)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

