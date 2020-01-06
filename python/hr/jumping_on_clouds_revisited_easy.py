#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
  e = 100
  cloud = -1
  while cloud != 0:
    if cloud == -1:
      cloud = 0
    cloud = (cloud + k) % len(c)
    e -= 1
    if c[cloud] == 1:
      e -= 2

  return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

