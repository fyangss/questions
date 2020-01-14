#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
  """
  Separate keep track of max and frequency map
  """
  freq_map = {}
  max_val = float('-inf')

  for i in ar:
    if i > max_val:
      max_val = i
    # really slow apparently
    # freq_map[i] = ar.count(i)
    if i in freq_map:
      freq_map[i] += 1
    else:
      freq_map[i] = 1

  return freq_map[max_val]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

