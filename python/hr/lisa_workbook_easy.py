#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
  page = 1
  special = 0

  for i in arr:
    probs_left_in_chapter = i
    cur_prob_index = 1

    # lazy
    while True:
      low = cur_prob_index
      if probs_left_in_chapter > k:
        probs_left_in_chapter -= k
        high = cur_prob_index + k - 1
        if page >= low and page <= high:
          special += 1
        cur_prob_index = high + 1
        page += 1
      else:
        high = cur_prob_index + probs_left_in_chapter - 1
        if page >= low and page <= high:
          special += 1
        page += 1
        break

  return special


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
