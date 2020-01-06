#!/bin/python3

import math
import os
import random
import re
import sys

def getIndex(arr, n):
  for i in range(len(arr)):
    if arr[i] == n:
      return i

def permutationEquation(p):
  n = len(p)
  ans = []

  for i in range(1,n+1):
    ans.append(getIndex(p, getIndex(p, i) + 1) + 1)
  return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

