#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
  values = {'pos': 0, 'neg': 0, 'zero': 0}
  for i in arr:
    if i > 0:
      values['pos'] += 1
    elif i < 0:
      values['neg'] += 1
    else:
      values['zero'] += 1
  print(values['pos']/len(arr))
  print(values['neg']/len(arr))
  print(values['zero']/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

