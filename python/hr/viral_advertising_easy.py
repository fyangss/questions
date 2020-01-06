#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
  share = 5
  cum_liked = 0
  for i in range(0,n):
    liked = int(share/2)
    cum_liked += liked
    share = liked * 3
  return cum_liked


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

