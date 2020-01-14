#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
  length = len(s)
  mod = n % length
  repeats = int(n/length)
  num_a = repeats * s.count('a')
  for i in s[:mod]:
    if i == 'a':
      num_a += 1

  return num_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
