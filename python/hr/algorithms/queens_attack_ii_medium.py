#!/bin/python3

import math
import os
import random
import re
import sys

def constraintChecker(x, y, delta_x, delta_y, n, squares, obs):
  while x <= n and y <= n and x > 0 and y > 0:
    tup = (x, y)
    if tup in obs:
      return
    squares[tup] = True
    x += delta_x
    y += delta_y

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
  squares = {}

  obs = {}
  for o in obstacles:
    obs[o[0], o[1]] = True

  directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
  for d in directions:
    constraintChecker(r_q, c_q, d[0], d[1], n, squares, obs)
  
  return len(squares) - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
