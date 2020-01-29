#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
  longest = 0
  alpha = 'abcdefghijklmnopqrstuvwxyz'

  for i in alpha:
    for j in alpha:
      if i == j:
        continue
      count = 0
      first = True
      for k in s:
        if first:
          if k == i:
            count += 1
            first = False
          elif k == j:
            count = 0
            break
        else:
          if k == j:
            count += 1
            first = True
          elif k == i:
            count = 0
            break
      longest = max(longest, count if count != 1 else 0)

  return longest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
