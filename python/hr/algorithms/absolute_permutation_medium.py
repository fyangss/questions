#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
  num = []
  if k == 0:
    for i in range(1, n+1):
      num.append(i)
    return num

  if n % (2*k) != 0:
    return [-1]

  up = True
  for i in range(1, n+1):
    if up:
      num.append(i+k)
    else:
      num.append(i-k)
    if i % k == 0:
      up = not up

  return num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

