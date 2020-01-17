#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
  rems = []
  for i in s:
    rems.append(i % k)

  max_rem = 0
  for i in range(1, int(k/2) + 1):
    if i == (k-i):
      max_rem += 1
    else:
      max_rem += max(rems.count(i), rems.count(k-i))

  if 0 in rems:
    max_rem += 1
  return max_rem


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
