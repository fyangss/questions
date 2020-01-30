#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):
  gems = set(arr[0])
  for i in arr:
    not_gem = []
    for g in gems:
      if g not in i:
        not_gem.append(g)
    for g in not_gem:
      gems.remove(g)
  return len(gems)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
