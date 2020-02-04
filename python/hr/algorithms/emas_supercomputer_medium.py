#!/bin/python3

import math
import os
import random
import re
import sys

def make_largest_cross(x, y, n, m, grid, grids):
  if grid[x][y] != 'G':
    return

  cur_largest = [(x,y)]
  grids.append(cur_largest.copy())
  l,r,u,d = (x,y), (x,y), (x,y), (x,y)
  while True:
    l = (l[0]-1, l[1])
    r = (r[0]+1, r[1])
    u = (u[0], u[1]-1)
    d = (d[0], d[1]+1)

    # this is fine
    die = False
    for i in [l, r, u, d]:
      if not(i[0] >= 0 and i[1] >= 0 and i[0] < n and i[1] < m):
        die = True
        break
      elif grid[i[0]][i[1]] != 'G':
        die = True
        break
    if die:
        break

    cur_largest.append(l)
    cur_largest.append(r)
    cur_largest.append(u)
    cur_largest.append(d)
    grids.append(cur_largest.copy())

def twoPluses(grid):
  n, m = len(grid), len(grid[0])
  grids = []

  for i in range(n):
    for j in range(m):
      make_largest_cross(i, j, n, m, grid, grids)

  max_area = -1
  for i in range(len(grids)):
    for j in range(i+1, len(grids)):
      works = True
      for k in grids[i]:
        if k in grids[j]:
          works = False
          break
      if works:
        max_area = max(max_area, len(grids[i]) * len(grids[j]))

  return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
