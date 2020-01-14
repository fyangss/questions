#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
  candy_left = m % n
  prisoner = s + candy_left - 1
  if prisoner > n:
    prisoner -= n
  if prisoner == 0:
    prisoner = n
  return prisoner

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()

