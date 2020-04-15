#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the anagram function below.
def anagram(s):
  if len(s) % 2 == 1:
    return -1

  s1 = s[:len(s)//2]
  s2 = s[len(s)//2:]
  d = defaultdict(int)

  for c in s1:
    d[c] += 1
  for c in s2:
    d[c] -= 1
  pos, neg = 0, 0
  for v in d.values():
    if v > 0:
      pos += v
    else:
      neg -= v
  
  if pos == neg:
    return pos
  else:
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
