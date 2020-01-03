#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
  freq_map = {}
  for i in ar:
    if i in freq_map:
      freq_map[i] += 1
    else:
      freq_map[i] = 1

  num_pairs = 0
  for index in freq_map:
    i = freq_map[index]
    while i > 1:
      i = i - 2
      num_pairs += 1

  return num_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

