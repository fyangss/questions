#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def bomberMan(n, grid):
  if n == 0 or n == 1:
    return grid

  mat = []
  for i in grid:
    mat.append(['O' for _ in i])

  out = []
  if n % 2 == 0:
    for i in mat:
      out.append(''.join(i))
    return out

  dirs = [(0,0), (1,0), (-1,0), (0, 1), (0, -1)]
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == 'O':
        for d in dirs:
          x = i + d[0]
          y = j + d[1]
          if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[i]):
            mat[x][y] = '.'

  phase1 = []
  for i in mat:
    phase1.append(''.join(i))
  
  mat = []
  for i in grid:
    mat.append(['O' for _ in i])

  for i in range(len(phase1)):
    for j in range(len(phase1[i])):
      if phase1[i][j] == 'O':
        for d in dirs:
          x = i + d[0]
          y = j + d[1]
          if x >= 0 and y >= 0 and x < len(phase1) and y < len(phase1[i]):
            mat[x][y] = '.'
  phase2 = []
  for i in mat:
    phase2.append(''.join(i))
  
  if n == 3 or (n-3) % 4 == 0:
    return phase1
  return phase2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()


