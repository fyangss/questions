#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
  max_score, min_score = scores[0], scores[0]
  break_max, break_min = 0, 0
  for i in scores[1:]:
    if i > max_score:
      max_score = i
      break_max += 1
    elif i < min_score:
      min_score = i
      break_min += 1

  return [break_max, break_min]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

