#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(n, s):
  alt = 0
  valleys = 0
  in_valley = False
  for i in s:
    if i == 'U':
      alt += 1
      if alt == 0 and in_valley:
        in_valley = False
        valleys += 1
    else:
      if alt == 0:
        in_valley = True
      alt -= 1

  return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

