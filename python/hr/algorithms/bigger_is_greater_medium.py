#!/bin/python3

import math
import os
import random
import re
import sys

def increase(string):
  for i in range(len(string) - 2, -1, -1):
    if string[i] < string[i + 1]:
      return i
  return -1

def min_greater(string, index):
  min_index = index+1
  for i in range(index+1, len(string)):
    if string[i] > string[index] and string[index] < string[min_index]:
      min_index = i
  return min_index
  
def swap(string, i1, i2):
  swapped = list(string)
  swapped[i1], swapped[i2] = swapped[i2], swapped[i1]
  return ''.join(swapped)
  
def sort_rest(string, i):
  start = string[:i]
  end = list(string[i:])
  end.sort()
  return start + ''.join(end)

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
  if len(w) == 1:
    return 'no answer'

  inc = increase(w)
  if inc == -1:
    return 'no answer'

  new_string = swap(w, inc, min_greater(w, inc))
  return sort_rest(new_string, inc + 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
