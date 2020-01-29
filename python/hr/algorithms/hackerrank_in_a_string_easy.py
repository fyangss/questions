#!/bin/python3

import math
import os
import random
import re
import sys

def search(search_string, rem_string):
  if len(rem_string) < len(search_string):
    return False
  elif len(search_string) == 0:
    return True
  elif len(search_string) == 1:
    for i in rem_string:
      if i == search_string:
        return True
    return False
  elif len(search_string) == 2:
    for i in range(len(rem_string)):
      if rem_string[i] == search_string[0]:
        for j in range(i+1, len(rem_string)):
          if rem_string[j] == search_string[1]:
            return True
    return False
  else:
    letter = search_string[0]
    for i in range(len(rem_string)):
      if rem_string[i] == letter:
        if search(search_string[1:], rem_string[i+1:]):
          return True
    return False

# Complete the hackerrankInString function below.
def hackerrankInString(s):
  return 'YES' if search('hackerrank', s) else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
