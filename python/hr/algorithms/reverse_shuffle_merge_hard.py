#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
  freq = defaultdict(int)
  for i in s:
    freq[i] += 1

  used = defaultdict(int)
  remaining = freq.copy()
  out = []

  for i in s[::-1]:
    if used[i] < (freq[i] // 2):
      while out and out[-1] > i and (used[out[-1]] + remaining[out[-1]] > (freq[out[-1]] // 2)):
        removed = out.pop()
        used[removed] -= 1

      used[i] += 1
      out.append(i)
    remaining[i] -= 1

  return ''.join(out)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
