#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
  tl, tr, bl, br = (0,0), (0,len(matrix[0])-1), (len(matrix)-1,0), (len(matrix)-1,len(matrix[0])-1)
  while tl < br and tl < tr:
    rots = r % ((2*(tr[1]-tl[1]+1) + 2*(bl[0]-tl[0]+1)) - 4)
    for _ in range(rots):
      top_left = matrix[tl[0]][tl[1]]

      for i in range(tl[1], tr[1]):
        matrix[tl[0]][i] = matrix[tl[0]][i+1]

      for i in range(tr[0], br[0]):
        matrix[i][tr[1]] = matrix[i+1][tr[1]]

      for i in range(br[1], bl[1], -1):
        matrix[br[0]][i] = matrix[br[0]][i-1]

      for i in range(bl[0], tl[0], -1):
        matrix[i][bl[1]] = matrix[i-1][bl[1]]

      matrix[tl[0]+1][tl[1]] = top_left

    tl = (tl[0]+1, tl[1]+1)
    tr = (tr[0]+1, tr[1]-1)
    bl = (bl[0]-1, bl[1]+1)
    br = (br[0]-1, br[1]-1)

  for i in matrix:
    print(' '.join(map(str,i)))


if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
