#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
  msg = 'SOS'
  mi = 0
  counter = 0
  for i in s:
    if i != msg[mi]:
      counter += 1
    mi = (mi + 1) % 3
  return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
