#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
  l, r = 0, len(s)-1
  reducs = 0
  while l < r:
    reducs += abs(ord(s[l]) - ord(s[r]))
    l += 1
    r -= 1
  return reducs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
