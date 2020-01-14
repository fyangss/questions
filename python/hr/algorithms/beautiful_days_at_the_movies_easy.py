#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def isBDay(n, k):
  reverse = int(str(n)[::-1])
  return abs(n - reverse) % k == 0

def beautifulDays(i, j, k):
  days = 0
  for x in range(i,j+1):
    days += 1 if isBDay(x,k) else 0
  return days


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()

