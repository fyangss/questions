#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
  a = B
  loaves = 0
  for i in range(len(a)-1):
    if a[i] % 2 == 1:
      a[i] += 1
      a[i+1] += 1
      loaves += 2
  return loaves if a[-1] % 2 == 0 else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
