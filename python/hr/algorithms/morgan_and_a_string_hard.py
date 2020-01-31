#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the morganAndString function below.
def morganAndString(a, b):
  a = a+'z'
  b = b+'z'

  out = []
  a_iter, b_iter = 0, 0
  while a_iter < len(a)-1 and b_iter < len(b)-1:
    if a[a_iter] > b[b_iter]:
      out.append(b[b_iter])
      b_iter += 1
    elif a[a_iter] < b[b_iter]:
      out.append(a[a_iter])
      a_iter += 1
    else:
      if a[a_iter:] <= b[b_iter:]:
        out.append(a[a_iter])
        a_iter += 1
      else:
        out.append(b[b_iter])
        b_iter += 1
  while a_iter < len(a)-1:
    out.append(a[a_iter])
    a_iter += 1
  while b_iter < len(b)-1:
    out.append(b[b_iter])
    b_iter += 1

  return ''.join(out)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()
