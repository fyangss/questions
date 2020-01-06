#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
  index = len(s)
  for i in range(len(s)):
    if i >= len(t):
      index = i
      break
    if s[i] != t[i]:
      index = i
      break
  moves = (len(s) - index) + (len(t) - index)

  if k >= max(len(s), len(t)) * 2:
    return 'Yes'
  if k < moves:
    return 'No'
  if k == moves:
    return 'Yes'
  if (k - moves) % 2 == 0:
    return 'Yes'
  return 'Yes' if (k - moves) >= (index * 2) else 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()

