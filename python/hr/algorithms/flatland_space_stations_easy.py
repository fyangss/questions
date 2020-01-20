#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
  c.sort()
  max_in_between = -1
  for i in range(len(c)-1):
    max_in_between = max(max_in_between, int(abs(c[i+1] - c[i])/2))

  return max(abs(c[0] - 0), abs(c[-1] - (n - 1)), max_in_between)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
