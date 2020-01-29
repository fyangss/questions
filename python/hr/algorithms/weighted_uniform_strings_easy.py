#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
  nums = set()
  prev = -1 
  repeats = 1
  for i in s:
    if i != prev:
      prev = i
      repeats = 1
    else:
      repeats += 1
    nums.add(repeats * (ord(i) - ord('a') + 1))

  return ['Yes' if q in nums else 'No' for q in queries]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
