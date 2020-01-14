#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
  div = []
  non_div = []
  pairs = 0

  for i in range(len(ar)):
    for j in ar[i+1:]:
      val = ar[i] + j
      if val in non_div:
        continue
      if val in div:
        pairs += 1
        continue

      if val % k == 0:
        div.append(val)
        pairs += 1
      else:
        non_div.append(val)

  return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

