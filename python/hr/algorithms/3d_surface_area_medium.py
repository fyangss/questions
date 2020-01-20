#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(a):
  dirs = [(1,0), (0,1), (-1,0), (0,-1)]

  area = 0
  for i in range(len(a)):
    for j in range(len(a[0])):
      area += 2
      for d in dirs:
        x, y = i+d[0], j+d[1]
        if x in range(len(a)) and y in range(len(a[0])):
          if a[i][j] > a[x][y]:
            area += a[i][j] - a[x][y]
        else:
          area += a[i][j]
          
  return area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
