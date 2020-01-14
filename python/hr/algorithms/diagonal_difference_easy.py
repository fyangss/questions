#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
  """
  Just build diagonals and add them together
  Var names are the shape they name on the matrix :S
  """
  backslash = 0
  forwardslash = 0

  for i in range(len(arr)):
    cur_list = arr[i]
    backslash += cur_list[i]
    forwardslash += cur_list[len(arr)-1-i]

  return abs(backslash - forwardslash)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

