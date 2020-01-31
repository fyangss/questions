#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
  s = arr.copy()
  s.sort()

  wrong = []
  for i in range(len(arr)):
    if arr[i] != s[i]:
      wrong.append(i)
  
  if len(wrong) == 2:
    maybe = arr.copy()
    maybe[wrong[0]], maybe[wrong[1]] = maybe[wrong[1]], maybe[wrong[0]]
    if maybe == s:
      wrong = [i+1 for i in wrong]
      print('yes')
      print('swap', ' '.join(map(str, wrong)))
      return
    else:
      print('no')
      return
  
  middle = []
  for i in range(wrong[-1], wrong[0] - 1, -1):
    middle.append(arr[i])

  maybe = arr[:wrong[0]] + middle + arr[wrong[-1] + 1:]

  if maybe == s:
    wrong = [i+1 for i in wrong]
    print('yes')
    print('reverse', wrong[0], wrong[-1])
  else:
    print('no')


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
