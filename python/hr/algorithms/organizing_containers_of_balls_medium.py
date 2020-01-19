#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
  freq = {}
  for i in range(len(container)):
    row_sum = 0
    col_sum = 0
    for j in range(len(container)):
      row_sum += container[i][j]
      col_sum += container[j][i]

    if row_sum in freq:
      freq[row_sum] += 1
    else:
      freq[row_sum] = 1
    
    if col_sum in freq:
      freq[col_sum] -= 1
    else:
      freq[col_sum] = -1
    
  for i in freq:
    if freq[i] != 0:
      return 'Impossible'
  
  return 'Possible'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
