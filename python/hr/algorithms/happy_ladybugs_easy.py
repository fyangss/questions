#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
  temp = []
  for i in range(len(b)):
    temp.append(b[i])
  b = temp
  freq = {}
  for i in b:
    if i in freq:
      freq[i] += 1
    else:
      freq[i] = 1
  
  if '_' not in freq:
    for i in range(len(b)):
      if i - 1 >= 0:
        if b[i] == b[i-1]:
          continue
      if i + 1 < len(b):
        if b[i] == b[i+1]:
          continue
      return 'NO'
    return 'YES'

  for i in freq:
    if i != '_' and freq[i] == 1:
      return 'NO'
  return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
