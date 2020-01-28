#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
  for i in range(1, len(arr)):
    for j in range(i-1, -1, -1):
      if arr[j] > arr[j+1]:
        arr[j+1], arr[j] = arr[j], arr[j+1]
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
