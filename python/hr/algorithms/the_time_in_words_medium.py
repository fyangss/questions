#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
  num_word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
  minutes = ' minutes'
  if m == 0 or m == 15 or m == 30 or m == 45:
    minutes = ''
  if m == 1:
    minutes = ' minute'
  if m == 0:
    return num_word[h] + ' o\' clock'
  elif m == 30:
    return 'half past ' + num_word[h]
  elif m < 30:
    if m > 20:
      return 'twenty ' + num_word[m - 20] + minutes + ' past ' + num_word[h]
    else:
      return num_word[m] + minutes + ' past ' + num_word[h]
  else:
    diff = 60 - m
    if h + 1 == 13:
      h = 0
    if diff > 20:
      return 'twenty ' + num_word[diff - 20] + minutes + ' to ' + num_word[h+1]
    else:
      return num_word[diff] + minutes + ' to ' + num_word[h+1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
