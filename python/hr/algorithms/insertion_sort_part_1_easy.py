#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
  num = arr[-1]
  for i in range(len(arr)-1, 0, -1):
    if arr[i-1] > num:
      arr[i] = arr[i-1]
      print(' '.join(map(str, arr)))
    else:
      arr[i] = num
      print(' '.join(map(str, arr)))
      return
  arr[0] = num
  print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
