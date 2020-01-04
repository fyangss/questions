#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
  pages_turned = 0
  if p == 1 or p == n:
    return pages_turned

  if n / 2 < p:
    if n % 2 == 1:
      return int((n - p)/2)
    else:
      return int((n - p + 1)/2)
  else:
    return int(p/2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

