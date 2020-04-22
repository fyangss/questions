#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
  d = defaultdict(int)
  for i in range(len(arr)):
    v = arr[i]
    if d[m-v] != 0:
      return [min(i+1, d[m-v]), max(i+1, d[m-v])]
    else:
      d[v] = i+1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
