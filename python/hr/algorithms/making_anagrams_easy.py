#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
  d = defaultdict(int)
  for c in s1:
    d[c] += 1
  for c in s2:
    d[c] -= 1
  ans = 1
  for v in d.values():
    ans += abs(v)
  return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
