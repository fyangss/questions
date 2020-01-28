#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    buckets = []
    for _ in range((10**6)+1):
      buckets.append([])
    
    for _ in range(n):
      item = input()
      buckets[len(item)].append(item)
    
    for b in buckets:
      b.sort()
    
    for b in buckets:
      if b != []:
        fptr.write('\n'.join(b))
        fptr.write('\n')

    fptr.close()
