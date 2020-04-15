#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the gameOfThrones function below.
def gameOfThrones(s):
  d = defaultdict(int)
  for c in s:
    d[c] += 1
  if len(s) % 2 == 0:
    for v in d.values():
      if v % 2 != 0:
        return 'NO'
    return 'YES'
  else:
    odd = False
    for v in d.values():
      if v % 2 != 0:
        if odd:
          return 'NO' 
        else:
          odd = True
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
