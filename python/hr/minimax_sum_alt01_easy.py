#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
  min_val = float('inf')
  max_val = float('-inf')

  arr_sum = 0
  for i in arr:
    if i < min_val:
      min_val = i
    if i > max_val:
      max_val = i
    arr_sum += i

  print(str(arr_sum-max_val) + ' ' + str(arr_sum-min_val))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

