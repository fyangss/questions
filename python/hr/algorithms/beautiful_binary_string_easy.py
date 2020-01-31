#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
  if len(b) < 3:
    return 0

  count = 0
  i = 0
  while i < len(b) - 2:
    if b[i] == '0' and b[i+1] == '1' and b[i+2] == '0':
      if i > len(b) - 5:
        count += 1
        i += 2
      elif b[i+3] == '1' and b[i+4] == '0':
        count += 1
        i += 4
      else:
        count += 1
        i += 2
    else:
      i += 1

  return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
