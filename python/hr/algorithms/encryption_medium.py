#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
  no_space = s.replace(' ', '')
  rows = int(math.sqrt(len(no_space)))
  cols = rows
  if cols * rows < len(no_space):
    cols += 1

  cur_row = []
  new_text = []
  for i in range(len(no_space)):
    cur_row.append(no_space[i])
    if (i + 1) % cols == 0 or i == len(no_space) - 1:
      new_text.append(cur_row)
      cur_row = []

  encrypted = ''
  for i in range(len(new_text[0])):
    for j in range(len(new_text)):
      if i >= len(new_text[j]):
        break
      encrypted += new_text[j][i]
    encrypted += ' '

  return encrypted

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
