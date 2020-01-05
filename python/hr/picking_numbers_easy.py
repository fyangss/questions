#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
  max_sub = -1
  for i in range(len(a)):
    pos_sub = 1
    neg_sub = 1
    for j in a[i+1:]:
      diff = j - a[i]
      if diff == 0:
        pos_sub += 1
        neg_sub += 1
      elif diff == 1:
        pos_sub += 1
      elif diff == -1:
        neg_sub += 1
    max_sub = max(max_sub, max(pos_sub, neg_sub))
  return max_sub

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

