#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(a):
  for i in range(len(a) - 3):
    ind = a.index(i+1)
    if i == ind:
      continue
    elif (ind - i) % 2 == 0:
      a[i], a[i+1:ind+1] = a[ind], a[i:ind]
    else:
      a[i], a[i+1:ind+1] = a[ind], a[i:ind]
      a[i+1], a[i+2] = a[i+2], a[i+1]

  if a[-3] - a[-2] == -1 or a[-3] - a[-2] == 2:
    return 'YES'
  else:
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
