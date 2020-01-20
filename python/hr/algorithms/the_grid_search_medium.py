#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(g, p):
  candidates = []
  for row in range(len(g) - len(p) + 1):
    for col in range(len(g[0]) - len(p[0]) + 1):
      if g[row][col:col+len(p[0])] == p[0]:
        candidates.append((row, col))
  
  for c in candidates:
    x, y = c[0], c[1]
    found = True
    for i in range(1, len(p)):
      if g[x+i][y:y+len(p[0])] != p[i]:
        found = False
        break
    if found:
      return 'YES'
  return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
