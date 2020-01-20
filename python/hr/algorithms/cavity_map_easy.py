#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
  dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
  out = []
  for x in range(len(grid)):
    row = ''
    for y in range(len(grid[0])):
      item = str(grid[x][y])
      if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[0]) - 1:
        row += item
      else:
        set_item = False
        for d in dirs:
          if grid[x+d[0]][y+d[1]] >= grid[x][y]:
            set_item = True
            break
        if set_item:
          row += item
        else:
          row += 'X'
    out.append(row)
  return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = list(map(int, [x for x in (input())[:]]))
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
