#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
  """
  Brute force, basic math / number theory too hard T_T
  """
  a,b = list(set(a)), list(set(b))
  reduced_a, reduced_b = [], []
  a.sort()
  b.sort()
  for i in range(len(a)):
    add = True
    for j in range(i+1,len(a)):
      if j < len(a) and a[j] % a[i] == 0:
        add = False
        break
    if add:
      reduced_a.append(a[i])

  blacklist = set()
  for i in range(len(b)):
    if b[i] in blacklist:
      continue
    for j in range(i+1,len(b)):
      if j < len(b) and b[j] % b[i] == 0:
        blacklist.add(b[j])
    reduced_b.append(b[i])

  cur_val, stop = max(reduced_a), min(reduced_b)
  step = cur_val

  output = 0
  print(reduced_a)
  print(reduced_b)

  while cur_val <= stop:
    go_next = False
    for i in reduced_a:
      if cur_val % i != 0:
        go_next = True
        break
    if go_next:
      cur_val += step
      continue

    for i in reduced_b:
      if i % cur_val != 0:
        go_next = True
        break
    if go_next:
      cur_val += step
      continue

    output += 1
    cur_val += step

  return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

