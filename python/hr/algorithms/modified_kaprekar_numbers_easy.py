#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
  nums = []
  for i in range(p, q+1):
    n = str(i)
    d = len(n)
    pow2 = str(i**2)
    left = int(pow2[:len(pow2)-d] if pow2[:len(pow2)-d] != '' else '0')
    right = int(pow2[len(pow2)-d:] if pow2[len(pow2)-d:] != '' else '0')
    if left + right == i:
      nums.append(n)
  
  if len(nums) == 0:
    print('INVALID RANGE')
  else:
    print(' '.join(nums))

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
