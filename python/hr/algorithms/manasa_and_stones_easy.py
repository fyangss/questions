#!/bin/python3

import math
import os
import random
import re
import sys

def stones(n, a, b):
  out = [0]
  if n == 1:
    return out

  out = set(out)
  for _ in range(n-1):
    new_out = set()
    for i in out:
      new_out.add(i+a)
    for i in out:
      new_out.add(i+b)
    out = new_out
  out = list(out)
  out.sort()
  return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
