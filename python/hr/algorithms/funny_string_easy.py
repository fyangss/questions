#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
  diffs = []
  for i in range(len(s) - 1):
    diffs.append(abs(ord(s[i+1]) - ord(s[i])))

  d = 0
  for i in range(len(s) - 1, 0, -1):
    if abs(ord(s[i-1]) - ord(s[i])) != diffs[d]:
      return 'Not Funny'
    d += 1
  return 'Funny'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
